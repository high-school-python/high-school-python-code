"""整理されていないコードの例"""

print("クラス名簿管理プログラム")
name = input("名前を入力してください：")
age = int(input("年齢を入力してください："))
current_year = 2024
birth_year = current_year - age
blood_type = input("血液型を入力してください：")
height = float(input("身長を入力してください（cm）："))
weight = float(input("体重を入力してください（kg）："))
height_m = height / 100
bmi = weight / (height_m**2)
message = "【個人データ】\n"
message += f"名前：{name}\n"
message += f"年齢：{age}歳（{birth_year}年生まれ）\n"
message += f"血液型：{blood_type}型\n"
message += f"身長：{height}cm\n"
message += f"体重：{weight}kg\n"
message += f"BMI 値：{bmi:.1f}"
print(message)


"""整理されたコードの例"""


def get_personal_info() -> tuple[str, int, str]:
    """個人情報を入力して取得する.

    Returns:
        tuple[str, int, str]: 名前, 年齢, 血液型
    """
    name = input("名前を入力してください：")
    age = int(input("年齢を入力してください："))
    blood_type = input("血液型を入力してください：")

    return name, age, blood_type


def get_physical_info() -> tuple[float, float]:
    """身体情報を入力して取得する.

    Returns:
        tuple[float, float]: 身長, 体重
    """
    height = float(input("身長を入力してください（cm）："))
    weight = float(input("体重を入力してください（kg）："))

    return height, weight


def calculate_birth_year(age: int) -> int:
    """年齢から生年を計算する.

    Args:
        age (int): 年齢

    Returns:
        int: 生年
    """
    current_year = 2024

    return current_year - age


def calculate_bmi(height: float, weight: float) -> float:
    """BMI を計算する.

    Args:
        height (float): 身長
        weight (float): 体重

    Returns:
        float: BMI値
    """
    return weight / (height_m**2)


def create_profile(
    name: str, age: int, birth_year: int, blood_type: str, height: float, weight: float, bmi: float
) -> str:
    """プロフィール文字列を作成する関数.

    Args:
        name (str): 名前
        age (int): 年齢
        birth_year (int): 生年
        blood_type (str): 血液型
        height (float): 身長
        weight (float): 体重
        bmi (float): BMI値

    Returns:
        str: プロフィール文字列
    """
    message = "【個人データ】\n"
    message += f"名前：{name}\n"
    message += f"年齢：{age}歳（{birth_year}年生まれ）\n"
    message += f"血液型：{blood_type}型\n"
    message += f"身長：{height}cm\n"
    message += f"体重：{weight}kg\n"
    message += f"BMI 値：{bmi:.1f}"

    return message


def main() -> None:
    """メインの処理を行う関数"""
    print("クラス名簿管理プログラム")

    # 個人情報の入力
    name, age, blood_type = get_personal_info()

    # 身体情報の入力
    height, weight = get_physical_info()

    # 各種計算
    birth_year = calculate_birth_year(age)
    bmi = calculate_bmi(height, weight)

    # プロフィール作成と表示
    profile = create_profile(name, age, birth_year, blood_type, height, weight, bmi)
    print("\n" + profile)


# プログラムの実行
if __name__ == "__main__":
    main()
