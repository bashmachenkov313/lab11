from flask import Flask
import math

app = Flask(__name__)


@app.route('/')
def greeting():
    greet = """
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask_calc</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <p>1.Для перехода к основным функциям калькулятора добавить к строке поиска - /primary_functions/</p>
    <p>Через / указать нужное выражение</p>
    <p>Функционал:</p>
    <p>1.Сложение</p>
    <p>2.Вычитание</p>
    <p>3.Умножение</p>
    <p>4.Деление(Вводить через ":")</p>
    <p>5.Корень(Вводить через sqrt) (пример 4 sqrt 2)</p>
    <p>6.Степень(Вводить через **)</p>
    <p>7.Целочисленное деление(Вводить через "::")</p>
    <p>8.Остаток от деления(Вводить через !)</p><br>
    <p>2.Для перехода к тригонометрическим функциям калькулятора добавить к строке поиска - /trigonometry_functions/ </p>
    <p>Через / указать нужное выражение (пример - cos 90 )</p>
    <p>Функционал:</p>
    <p>1.Синус(Вводить через sin)</p>
    <p>2.Косинус(Вводить через cos)</p>
    <p>3.Тангенс(Вводить через tg)</p>
    <p>4.Котангенс(Вводить через ctg)</p>
    <p>5.Арксинус(Вводить через asin)</p>
    <p>6.Арккосинус(Вводить через acos)</p>
</body>
</html>
    """
    return greet

@app.route('/primary_functions/<do>')
def calculate_primary(do:str) -> str:
    try:
        if ":" in do:
            do = do.replace(":","/")
        elif "!" in do:
            do = do.replace("!","%")
        elif "sqrt" in do:
            parts = do.split()
            if float(parts[0]) < 0 or float(parts[2]) < 0:
                return "Числа в корне не могут быть меньше нуля"
            else:
                return f"{do} = {str(pow(float(parts[0]), 1/float(parts[2])))}"
        return f"{do} = {str(eval(do))}"
    except Exception as ex:
        return str(ex)


@app.route('/trigonometry_functions/<do>')
def calculate_trigonometry(do: str) -> str:
    try:
        parts = do.split()
        result = ""
        if 'cos' in do:
            if -1 <= float(parts[1]) <= 1:
                result = math.cos(float(parts[1]))
            else:
                return 'В функцию передано неверное значение'
            return f"{do} = {result}"
        elif 'sin' in do:
            if -1 <= float(parts[1]) <= 1:
                result = math.sin(float(parts[1]))
            else:
                return 'В функцию передано неверное значение'
            return f"{do} = {result}"
        elif 'tg' in do:
            result = math.tan(float(parts[1]))
            return f"{do} = {result}"
        elif 'ctg' in do:
            result = (math.cos(float(parts[1]) / math.sin(float(parts[1]))))
            return f"{do} = {result}"
        elif 'acos' in do:
            if -1 <= float(parts[1]) <= 1:
                result = math.acos(float(parts[1]))
            else:
                return 'В функцию передано неверное значение'
            return f"{do} = {result}"
        elif 'asin' in do:
            if -1 <= float(parts[1]) <= 1:
                result = math.asin(float(parts[1]))
            else:
                return 'В функцию передано неверное значение'
            return f"{do} = {result}"
        return f"Я не знаю такого действия"
    except Exception as ex:
        return str(ex)

