#!/usr/bin/env python3
"""
Skill Create - 简化版skill安装工具

统一的skill安装、更新和管理工具，适配任何skill项目。
"""

import os
import sys
import json
import subprocess
import shutil
from typing import Dict, List, Optional
from pathlib import Path


class SkillCreateTool:
    """Skill创建和管理工具。"""

    # ===== 配置文件名 =====
    SKILLS_CONFIG_FILE = "skills_config.json"
    INSTALLED_SKILLS_FILE = "installed_skills.json"

    # ===== 默认配置 =====
    DEFAULT_SKILLS_DIR = ".skills"
    DEFAULT_SKILL_TEMPLATE = {
        "name": "skill-name",
        "version": "1.0.0",
        "description": "Skill description",
        "author": "Author name",
        "license": "MIT",
        "dependencies": {"required": [], "optional": []},
        "main_file": "main.py",
        "files": [],
        "commands": [],
        "env_vars": [],
    }

    # ===== 预定义的skill仓库 =====
    KNOWN_SKILL_REPOS = {
        "vercel-labs/agent-skills": "https://github.com/vercel-labs/agent-skills",
        "ComposioHQ/awesome-claude-skills": "https://github.com/ComposioHQ/awesome-claude-skills",
        "openai/openai-cookbook": "https://github.com/openai/openai-cookbook",
        "anthropics/anthropic-cookbook": "https://github.com/anthropics/anthropic-cookbook",
    }

    def __init__(self, project_dir: str = None):
        """
        初始化工具。

        Args:
            project_dir: 项目根目录路径（默认为当前目录）
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        self.skills_dir = self.project_dir / self.DEFAULT_SKILLS_DIR
        self.config_file = self.project_dir / self.SKILLS_CONFIG_FILE
        self.installed_file = self.project_dir / self.INSTALLED_SKILLS_FILE

        # 确保目录存在
        self.skills_dir.mkdir(exist_ok=True)

    # ===== 配置管理 =====
    def load_config(self) -> Dict:
        """加载skills配置。"""
        if self.config_file.exists():
            with open(self.config_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_config(self, config: Dict) -> None:
        """保存skills配置。"""
        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)

    def load_installed(self) -> Dict:
        """加载已安装的skills列表。"""
        if self.installed_file.exists():
            with open(self.installed_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_installed(self, installed: Dict) -> None:
        """保存已安装的skills列表。"""
        with open(self.installed_file, "w", encoding="utf-8") as f:
            json.dump(installed, f, ensure_ascii=False, indent=2)

    # ===== Skill操作 =====
    def list_skills(self) -> List[str]:
        """列出所有skills。"""
        if not self.skills_dir.exists():
            return []

        skills = []
        for skill_dir in self.skills_dir.iterdir():
            if skill_dir.is_dir():
                skills.append(skill_dir.name)

        return sorted(skills)

    def skill_exists(self, skill_name: str) -> bool:
        """检查skill是否存在。"""
        skill_dir = self.skills_dir / skill_name
        return skill_dir.exists() and skill_dir.is_dir()

    def get_skill_info(self, skill_name: str) -> Optional[Dict]:
        """获取skill信息。"""
        skill_json = self.skills_dir / skill_name / "skill.json"
        if skill_json.exists():
            with open(skill_json, "r", encoding="utf-8") as f:
                return json.load(f)
        return None

    # ===== 快速创建 =====
    def quick_create(
        self,
        name: str,
        description: str = "",
        main_file: str = "main.py",
        files: List = None,
        commands: List = None,
        env_vars: List = None,
        author: str = "IELTS Practice Project",
        license: str = "MIT",
    ) -> str:
        """
        快速创建skill。

        Args:
            name: skill名称
            description: 描述
            main_file: 主文件
            files: 额外文件列表
            commands: 运行命令列表
            env_vars: 环境变量列表
            author: 作者
            license: 许可证

        Returns:
            创建的skill路径
        """
        skill_dir = self.skills_dir / name

        # 检查是否已存在
        if skill_dir.exists():
            print(f"⚠️  Skill '{name}' 已存在")
            return str(skill_dir)

        # 创建skill目录
        skill_dir.mkdir()

        # 创建skill.json
        skill_config = {
            "name": name,
            "version": "1.0.0",
            "description": description,
            "author": author,
            "license": license,
            "dependencies": {"required": [], "optional": []},
            "main_file": main_file,
            "files": files or [],
            "commands": commands or [],
            "env_vars": env_vars or [],
        }

        skill_json_path = skill_dir / "skill.json"
        with open(skill_json_path, "w", encoding="utf-8") as f:
            json.dump(skill_config, f, ensure_ascii=False, indent=2)

        # 创建主文件
        main_file_path = skill_dir / main_file
        with open(main_file_path, "w", encoding="utf-8") as f:
            main_content = f'''"""{description.strip()}

Main module file for {name} skill.

```python
import sys
from pathlib import Path

# 获取skill根目录
SKILL_DIR = Path(__file__).parent

# 导入主模块
try:
    from {name} import main
except ImportError:
    # Skill not yet installed
    from {name} import main as _main_module

def init():
    """Initialize skill if needed."""
    pass

if __name__ == "__main__":
    _main_module = _main_module if "_main_module" in locals() else None

    if _main_module is None:
        print("❌ Skill '{name}' is not installed yet.")
        sys.exit(1)

    # 调用初始化函数
    if hasattr(_main_module, "init"):
        _main_module.init()
        print(f"✅ Skill '{name}' initialized successfully!")
    else:
        print(f"✅ Skill '{name}' loaded!")
'''
            with open(main_file_path, "w", encoding="utf-8") as f:
                f.write(main_content)

        # 创建其他文件
        if files:
            for file_name in files:
                file_path = skill_dir / file_name
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("# Auto-generated file\n")

        # 更新已安装列表
        installed = self.load_installed()
        installed[name] = {
            "path": str(skill_dir),
            "version": "1.0.0",
            "installed_at": self._get_current_timestamp(),
        }
        self.save_installed(installed)

        return str(skill_dir)

    # ===== 辅助功能 =====
    def install_from_template(self, template: str, name: str) -> str:
        """
        从预定义模板安装skill。

        Args:
            template: 模板名称（来自KNOWN_SKILL_REPOS）
            name: skill名称

        Returns:
            创建的skill路径
        """
        if template not in self.KNOWN_SKILL_REPOS:
            print(f"❌ 未知模板: {template}")
            return ""

        repo_info = self.KNOWN_SKILL_REPOS[template]
        git_url = repo_info.get("git", f"https://github.com/{template}")

        skill_dir = self.skills_dir / name

        # 检查是否已存在
        if skill_dir.exists():
            print(f"⚠️  Skill '{name}' 已存在")
            return str(skill_dir)

        # 克隆模板
        print(f"📥 从模板克隆: {git_url}")

        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", git_url, str(skill_dir)],
                check=True,
                capture_output=True,
            )
            print(f"✅ 克隆成功")
        except subprocess.CalledProcessError as e:
            print(f"❌ 克隆失败: {e}")
            return ""

        # 重命名skill.json
        original_json = skill_dir / ".git" / "skill.json"
        target_json = skill_dir / "skill.json"
        if original_json.exists():
            os.rename(original_json, target_json)

        # 更新skill.json中的信息
        with open(target_json, "r", encoding="utf-8") as f:
            config = json.load(f)

        config["name"] = name
        config["description"] = f"Based on {template}"
        config["author"] = "IELTS Practice Project"

        with open(target_json, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)

        # 清理.git目录
        git_dir = skill_dir / ".git"
        if git_dir.exists():
            shutil.rmtree(git_dir)

        return str(skill_dir)

    def remove_skill(self, name: str) -> bool:
        """
        移除已安装的skill。

        Args:
            name: skill名称

        Returns:
            是否成功
        """
        skill_dir = self.skills_dir / name

        if not skill_dir.exists():
            print(f"❌ Skill '{name}' 不存在")
            return False

        # 删除skill目录
        import shutil

        shutil.rmtree(skill_dir)

        # 更新已安装列表
        installed = self.load_installed()
        if name in installed:
            del installed[name]
            self.save_installed(installed)

        print(f"✅ Skill '{name}' 已移除")
        return True

    def update_skill(self, name: str, **kwargs) -> bool:
        """
        更新skill配置。

        Args:
            name: skill名称
            **kwargs: 要更新的字段（key=value）

        Returns:
            是否成功
        """
        skill_json = self.skills_dir / name / "skill.json"
        if not skill_json.exists():
            print(f"❌ Skill '{name}' 不存在")
            return False

        with open(skill_json, "r", encoding="utf-8") as f:
            config = json.load(f)

        # 更新配置
        for key, value in kwargs.items():
            config[key] = value

        with open(skill_json, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)

        print(f"✅ Skill '{name}' 已更新")

        return True

    def validate_skill(self, name: str) -> Dict:
        """
        验证skill配置是否完整。

        Args:
            name: skill名称

        Returns:
            验证结果
        """
        skill_json = self.skills_dir / name / "skill.json"
        if not skill_json.exists():
            return {"valid": False, "errors": ["skill.json 不存在"]}

        with open(skill_json, "r", encoding="utf-8") as f:
            config = json.load(f)

        errors = []
        required_fields = ["name", "version", "description", "author"]

        for field in required_fields:
            if field not in config or not config[field]:
                errors.append(f"缺少必填字段: {field}")

        if not errors:
            return {"valid": True, "errors": []}

    def list_installed(self) -> Dict:
        """
        列出已安装的skills。

        Returns:
            已安装skills字典
        """
        if self.installed_file.exists():
            with open(self.installed_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _get_current_timestamp(self) -> str:
        """获取当前时间戳。"""
        from datetime import datetime

        return datetime.now().isoformat()

    def show_example(self, name: str):
        """显示skill使用示例。"""
        skill_json = self.skills_dir / name / "skill.json"
        if not skill_json.exists():
            print(f"❌ Skill '{name}' 不存在")
            return

        with open(skill_json, "r", encoding="utf-8") as f:
            config = json.load(f)

        print(f"\n📝 {name} Skill 使用示例")
        print("=" * 70)

        print(f"📋 Skill信息：")
        print(f"  名称: {config.get('name', name)}")
        print(f"  描述: {config.get('description', 'N/A')}")
        print(f"  主文件: {config.get('main_file', 'main.py')}")

        print(f"\n📄 安装方式：")
        print(f"  cd {name}")
        print(f"  python -m pip install {name}")

        print(f"\n🔧 使用方式：")
        print(f"  from {name} import main")
        print(f"  main.main()")

        print(f"\n" + "=" * 70)

    def _show_all_examples(self):
        """显示所有skill的使用示例。"""
        skills = self.list_skills()

        if not skills:
            print("❌ 没有可用的skills")
            return

        print("\n📝 所有Skill使用示例：")
        print("=" * 70)

        for skill in skills:
            self.show_example(skill)

    # ===== CLI命令 =====
    def run_cli(self):
        """运行CLI。"""
        import argparse

        parser = argparse.ArgumentParser(
            description="Skill Create - 统一的skill安装和管理工具",
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )

        subparsers = parser.add_subparsers(dest="command")

        # 创建命令
        create_parser = subparsers.add_parser("create", help="创建新的skill")
        create_parser.add_argument("name", help="Skill名称")
        create_parser.add_argument("-d", "--description", help="Skill描述")
        create_parser.add_argument("-m", "--main", help="主文件名（默认main.py）")
        create_parser.add_argument("-f", "--files", nargs="+", help="额外文件列表")
        create_parser.add_argument("-c", "--commands", nargs="+", help="运行命令列表")
        create_parser.add_argument("-e", "--env", nargs="+", help="环境变量列表")
        create_parser.add_argument(
            "--author", default="IELTS Practice Project", help="作者"
        )
        create_parser.add_argument("--license", default="MIT", help="许可证")

        install_parser = subparsers.add_parser("install", help="安装skill")
        install_parser.add_argument("name", help="Skill名称")
        install_parser.add_argument(
            "template", help="要安装的skill模板名称（列出所有可用skills）"
        )
        install_parser.add_argument("--name", nargs="?", help="要安装的skill名称")

        list_parser = subparsers.add_parser("list", help="列skills")
        list_parser.add_argument(
            "-i", "--installed", action="store_true", help="只显示已安装的"
        )

        remove_parser = subparsers.add_parser("remove", help="移除skill")
        remove_parser.add_argument("name", help="Skill名称")

        update_parser = subparsers.add_parser("update", help="更新skill配置")
        update_parser.add_argument("name", help="Skill名称")
        update_parser.add_argument("--name", nargs="+", help="要更新的字段（键=值）")

        example_parser = subparsers.add_parser("example", help="显示使用示例")
        example_parser.add_argument("name", help="Skill名称")

        validate_parser = subparsers.add_parser("validate", help="验证skill配置")
        validate_parser.add_argument("name", help="Skill名称")

        # 全局参数
        parser.add_argument("-v", "--verbose", action="store_true", help="详细输出")
        parser.add_argument(
            "--project-dir", default=str(self.project_dir), help="项目根目录"
        )

        args = parser.parse_args()

        # 执行命令
        if args.command == "create":
            if args.name and args.name in self.KNOWN_SKILL_REPOS:
                result = self.install_from_template(args.name, args.name)
            elif args.name:
                result = self.quick_create(
                    name=args.name,
                    description=args.description or "",
                    main_file=args.main,
                    files=args.files,
                    commands=args.commands,
                    env_vars=args.env_vars,
                    author=args.author,
                    license=args.license,
                )
            print(f"\n✅ 已创建: {result}")

        elif args.command == "install":
            if args.name:
                if args.template:
                    result = self.install_from_template(args.template, args.name)
                elif args.name:
                    result = self.quick_create(name=args.name, description="安装skill")
            else:
                skills = self.list_skills()
                if args.installed:
                    installed = self.load_installed()
                    print("\n📦 已安装的Skills：")
                    for name, info in installed.items():
                        print(f"  • {name}")
                        print(f"      路径: {info['path']}")
                        print(f"      版本: {info['version']}")
                        print(f"      安装时间: {info['installed_at']}")
                else:
                    skills = self.list_skills()
                    print("\n📚 可用的预定义模板：")
                    for template in self.KNOWN_SKILL_REPOS.items():
                        print(f"  • {template}: {template}")
                    print(f"\n💡 提供skill名称或使用 --template 列出所有")

        elif args.command == "list":
            skills = self.list_skills()
            installed = self.load_installed()

            if args.installed:
                print("\n📦 已安装的Skills：")
                for name, info in installed.items():
                    print(f"  • {name}")
                    print(f"      路径: {info['path']}")
                    print(f"      版本: {info['version']}")
                    print(f"      安装时间: {info['installed_at']}")
            else:
                skills = self.list_skills()
                print("\n📚 可用的Skills：")
                for skill in skills:
                    print(f"  • {skill}")

        elif args.command == "remove":
            result = self.remove_skill(args.name)
            if not args.verbose:
                print(f"\n✅ 已移除: {args.name}")

        elif args.command == "update":
            if args.name:
                updates = dict(zip(args.name[1::2], args.name[2::2]))
                result = self.update_skill(args.name, **updates)
            else:
                skills = self.list_skills()
                print("\n💡 提供skill名称或使用 --name 列出所有")

        elif args.command == "example":
            if args.name:
                self.show_example(args.name)
            else:
                self._show_all_examples()

        elif args.command == "validate":
            if args.name:
                validation = self.validate_skill(args.name)
                if validation["valid"]:
                    print(f"\n✅ Skill '{args.name}' 配置有效")
                else:
                    print(f"\n❌ Skill '{args.name}' 配置有误：")
                    for error in validation["errors"]:
                        print(f"  • {error}")
            else:
                skills = self.list_skills()
                print("\n💡 提供skill名称或使用 --name 列出所有")

    # ===== 工具功能 =====
    def is_global(self) -> bool:
        """检查是否全局安装。"""
        try:
            import skill_create_tool

            return True
        except ImportError:
            return False


def main():
    """主函数。"""
    tool = SkillCreateTool()

    try:
        tool.run_cli()
    except KeyboardInterrupt:
        print("\n\n⚠️  操作已取消")
    except Exception as e:
        print(f"\n\n❌ 错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
