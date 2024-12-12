import customtkinter as ctk
from tkinter import filedialog, messagebox
from moviepy.video.io.VideoFileClip import VideoFileClip
from PIL import Image
import os

def determine_slide_count(duration):

    if duration > 600:
        return 5
    elif 300 < duration <= 600:
        return 4
    elif 120 < duration <= 300:
        return 3
    else:
        return 2

def generate_slides_in_one_file(video_path, output_folder):

    try:
        os.makedirs(output_folder, exist_ok=True)

        with VideoFileClip(video_path) as clip:
            duration = clip.duration
            num_slides = determine_slide_count(duration)

            if num_slides == 1:
                timestamps = [duration / 2]
            else:
                first = duration * 0.18
                last = duration * 0.82
                timestamps = [first + i * (last - first) / (num_slides - 1) for i in range(num_slides)]

            frames = []

            for timestamp in timestamps:
                frame = clip.get_frame(timestamp)
                image = Image.fromarray(frame)
                frames.append(image)

            width, height = frames[0].size
            combined_height = height * num_slides
            combined_image = Image.new("RGB", (width, combined_height))

            for i, frame in enumerate(frames):
                combined_image.paste(frame, (0, i * height))

            video_name = os.path.splitext(os.path.basename(video_path))[0]
            output_path = os.path.join(output_folder, f"{video_name}.jpg")
            combined_image.save(output_path, format="JPEG", quality=95)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сгенерировать файл: {e}")

def select_videos():
    file_paths = filedialog.askopenfilenames(
        title="Выберите видео",
        filetypes=[("Видео файлы", "*.mp4 *.avi *.mov")]
    )
    if file_paths:
        video_path_entry.delete(0, ctk.END)
        video_path_entry.insert(0, "; ".join(file_paths))

def select_folder():
    folder_path = filedialog.askdirectory(title="Выберите папку для сохранения файлов")
    if folder_path:
        output_folder_entry.delete(0, ctk.END)
        output_folder_entry.insert(0, folder_path)

def start_generation():
    video_paths = video_path_entry.get().split("; ")
    output_folder = output_folder_entry.get()

    if not all(os.path.isfile(path) for path in video_paths):
        messagebox.showerror("Ошибка", "Один или несколько указанных видеофайлов не существуют!")
        return
    if not os.path.isdir(output_folder):
        messagebox.showerror("Ошибка", "Указанная папка не существует!")
        return

    for video_path in video_paths:
        generate_slides_in_one_file(video_path, output_folder)

    messagebox.showinfo("Успех", "Все файлы успешно сохранены!")

def main():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Генератор слайдов из видео")
    app.geometry("500x300")

    global video_path_entry, output_folder_entry

    video_path_label = ctk.CTkLabel(app, text="Путь к видео:")
    video_path_label.pack(pady=5)
    video_path_entry = ctk.CTkEntry(app, width=400)
    video_path_entry.pack(pady=5)
    select_video_button = ctk.CTkButton(app, text="Выбрать видео", command=select_videos)
    select_video_button.pack(pady=5)

    output_folder_label = ctk.CTkLabel(app, text="Папка для сохранения:")
    output_folder_label.pack(pady=5)
    output_folder_entry = ctk.CTkEntry(app, width=400)
    output_folder_entry.pack(pady=5)
    select_folder_button = ctk.CTkButton(app, text="Выбрать папку", command=select_folder)
    select_folder_button.pack(pady=5)

    generate_button = ctk.CTkButton(app, text="Сгенерировать файлы", command=start_generation)
    generate_button.pack(pady=20)

    app.mainloop()

if __name__ == "__main__":
    main()
