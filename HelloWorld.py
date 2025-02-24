# greet関数は、渡された名前を使って挨拶のメッセージを返します。
def greet(name: str) -> str:
    return f"Hello, {name}!"

# このスクリプトが直接実行された場合にのみ実行されるコードブロックです。
if __name__ == "__main__":
    # 挨拶するユーザー名を設定します。
    user_name = "World"
    # greet関数を呼び出して挨拶メッセージを表示します。
    print(greet(user_name))
