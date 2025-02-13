
"""このモジュールは、挨拶文を生成する関数を提供します.

このモジュールには、指定された名前に対して挨拶文を返す `greet` 関数が含まれています.
"""


def greet(name: str) -> str:
    """指定された名前に対して、挨拶文を返す関数です.

    Args:
        name (str): 挨拶する相手の名前。

    Returns:
        str: 挨拶のメッセージ。
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    # ユーザーに名前の入力を求め、その名前で挨拶を表示します。
    name = input("あなたの名前を入力してください: ")
    message = greet(name)
    print(message)
