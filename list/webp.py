from PIL import Image
import os

def convert_images_to_webp(root_directory):
    # 遍历目录及其子目录
    for root, _, files in os.walk(root_directory):
        for filename in files:
            if filename.endswith((".jpg", ".jpeg", ".png")):
                file_path = os.path.join(root, filename)
                # 打开图片文件
                with Image.open(file_path) as img:
                    # 构建输出文件路径，将扩展名改为.webp
                    output_filename = os.path.splitext(filename)[0] + ".webp"
                    output_path = os.path.join(root, output_filename)
                    # 转换为webp格式并保存
                    img.save(output_path, "webp")
                
                # 删除原始图片文件
                os.remove(file_path)

    print("图片转换并删除原文件完成！")

def generate_markdown_file(root_directory):
    # 遍历目录及其子目录
    image_files = []
    image_count = 0
    for root, _, files in os.walk(root_directory):
        for file in files:
            if file.endswith(".webp"):
                image_count += 1
                # 提取不包含扩展名的文件名作为名称
                image_name = os.path.splitext(file)[0]
                # 构建图片文件的链接，并进行路径处理
                relative_path = os.path.relpath(os.path.join(root, file), root_directory)
                # 将反斜杠替换为正斜杠，并加上 './'
                image_url = f"./{relative_path.replace(os.path.sep, '/')}"
                # 将信息添加到列表中，包括序号、名称和链接
                image_files.append(f"| {image_count} | {image_name} | [下载]({image_url}) |")

    # 清空或创建Markdown文件并写入表格内容
    with open("list.md", "w", encoding="utf-8") as md_file:
        # 写入Markdown表格的标题行和分隔行
        md_file.write("| #   | 名称                        | 链接                      |\n")
        md_file.write("| --- | --------------------------- | ------------------------- |\n")
        # 写入图片信息行
        md_file.write("\n".join(image_files))

    if image_files:
        print("已生成图片列表到 list.md 文件")
        print("\n".join(image_files))
    else:
        print("当前目录下没有图片文件")

# 获取当前目录
current_directory = os.getcwd()

# 执行图片转换和Markdown生成
convert_images_to_webp(current_directory)
generate_markdown_file(current_directory)
