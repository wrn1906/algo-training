import os
import sys

def create_workspace(contest_type, contest_no):
    # ベースとなるパスの設定
    base_path = os.path.dirname(os.path.abspath(__file__))
    contest_name = f"{contest_type}{contest_no}"
    
    # 作成する言語と拡張子の定義
    langs = {
        "cpp": "cpp",
        "py": "py"
    }

    # 各言語ごとにフォルダとファイルを作成
    for lang, ext in langs.items():
        # ディレクトリパス: workspace/cpp/abc/abc300
        target_dir = os.path.join(base_path, lang, contest_type, contest_name)
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            print(f"Created directory: {target_dir}")

        # AからG問題まで作成
        for problem in ["A", "B", "C", "D", "E", "F", "G"]:
            file_path = os.path.join(target_dir, f"{problem}.{ext}")
            
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    if ext == "cpp":
                        f.write(cpp_template)
                    else:
                        f.write(py_template)
                print(f"  Created file: {problem}.{ext}")

# --- テンプレート設定 ---
cpp_template = """#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    return 0;
}
"""

py_template = """import sys

def solve():
    # input = sys.stdin.read
    pass

if __name__ == "__main__":
    solve()
"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用法: python3 gen.py 300")
    else:
        create_workspace("abc", sys.argv[1])