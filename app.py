from flask import Flask, render_template, request

app = Flask(__name__)

# 定義技能字典
弱特_dict = {"1": 5, "2": 10, "3": 15, "4": 20, "5": 30}
看破_dict = {'1': 4, '2': 8, '3': 12, '4': 16, '5': 20}
抖擻_skill = {'1': 10, '2': 20, '3': 30}
ranger_skill = {'1': 3, '2': 5, '3': 7, '4': 10, '5': 15}
power_skill = {'1': 30, '2': 30, '3': 50, '4': 50, '5': 50}
poison_skill = {'1': 0, '2': 5, '3': 10, '4': 15, '5': 20}
dragon_skill = {'1': 3, '2': 6, '3': 10}
sword_skill = {'1': 50, '2': 75, '3': 100}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # 接收用戶輸入
        a = 弱特_dict[request.form['弱點特效']]
        b = 看破_dict[request.form['看破']]
        c = 抖擻_skill[request.form['精神抖擻']]
        d = ranger_skill[request.form['挑戰者']]
        e = power_skill[request.form['力量解放']]
        f = poison_skill[request.form['攻勢']]
        g = dragon_skill[request.form['無我之境']]

        # 計算會心率
        total_1 = a + b + c
        total_2 = total_1 + d + e + f + g

        # 顯示計算結果
        return render_template('index.html', total_1=total_1, total_2=total_2, d=d, e=e, f=f, g=g)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
