from flask import Flask, render_template

app = Flask(__name__)

# 假设这里有一些博客文章的数据
blog_posts = [
    {
        'title': '如何使用Python编写博客网站',
        'content': '这是一个关于使用Python和Flask编写博客网站的示例。',
        'author': '小明',
        'date_posted': '2024-02-17'
    },
    {
        'title': 'Flask框架入门指南',
        'content': 'Flask是一个轻量级的Python Web框架，非常适合快速开发。',
        'author': '小红',
        'date_posted': '2024-02-16'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=blog_posts)

@app.route('/about')
def about():
    return render_template('about.html', title='关于')

if __name__ == '__main__':
    app.run(debug=True)
