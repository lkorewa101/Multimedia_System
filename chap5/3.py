from PIL import Image

def check_image_formats():
    image_files = ['Dcu.png', 'sample.bmp', 'nuts.jpg']

    for image_file in image_files:
        try:
            with Image.open(image_file) as img:
                img_format = img.format

                if img_format == 'JPEG':
                    img_format = 'JPG'

                print(f"{image_file} 파일은 {img_format} 포맷 이미지입니다.")

        except FileNotFoundError:
            print(f"파일을 찾을 수 없음")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    check_image_formats()