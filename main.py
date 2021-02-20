from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
import pandas as pd
from portfolio import Portfolio

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

portfolio_list = []
portfolio_df = pd.read_csv("data.csv")
for index, row in portfolio_df.iterrows():
    portfolio_list.append(Portfolio(row["id"], row["name"], row["img_name"], row["detail"]))


@app.route('/')
def get_all_posts():
    return render_template("index.html", portfolio_list=portfolio_list)

@app.route('/portfolio/<int:id>', methods=["GET", "POST"])
def detail_portfolio(id):
    return render_template("detail.html", portfolio=portfolio_list[id-1])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)