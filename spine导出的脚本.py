import os

def export_project(project_path, output_path, export_json_path):
    command = f'Spine -i "{project_path}" -o "{output_path}" -e "{export_json_path}"'
    os.system(command)

# 输入输出文件夹和json导出设置文件路径
# Input/output folder and JSON export settings file path

input_dir = r"D:\动作序列帧训练素材\Q版武侠-暴走小虾米"
output_dir = r"D:\ex\outputspine"
json_path = r"D:\ex\exportJSON\22.export.json"

# 获取 input_dir 及其所有子文件夹中的所有 .spine 文件
# Get all.spine files in input_dir and all its subfolders

projects = []
for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.endswith('.spine'):
            project_path = os.path.join(root, file)
            
            # 输出路径文件夹
            # Output path folder
            
            filename = os.path.splitext(file)[0]
            output_filepath = output_dir
            if not os.path.exists(output_filepath):
                os.makedirs(output_filepath)
            projects.append((project_path, output_filepath, json_path))

# 批量执行导出操作
# Batch export operation

for project in projects:
    export_project(*project)
