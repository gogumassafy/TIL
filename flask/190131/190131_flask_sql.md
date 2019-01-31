# 190131_flask_sql

## 1. Pingpong:ping_pong:

- 실습 코드

  ```python
  from flask import Flask
  from flask import render_template, request
  
  @app.route('/ping')
  def ping():
      return render_template('ping.html')
      
  @app.route('/pong')
  def pong():
      pong = request.args.get('ping') # 
      return render_template('pong.html', pong=pong)
  ```

  - ping.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <h1>핑!</h1>
        <form action='/pong'>
            <input type="text" name="ping"/>
            <input type="submit" value="Submit"/>
        </form>
    </body>
    </html>
    ```

  - pong.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <h1>퐁!</h1>
        <h2>{{ pong }}</h2>
    </body>
    </html>
    ```

1.1. request.args는 ping에서 던진 값을 딕셔너리처럼 담아온다. 따라서 py에서 get을 쓰는 이유는 딕셔너리에서 값을 꺼내오기 위함이며 get을  쓰는 이유는 키가 없어도 오류를 출력하지 않기 때문.



- 실습코드2

  ```python
  from flask import Flask
  from flask import render_template, request
  
  @app.route('/ping_new')
  def ping_new():
      return render_template('ping_new.html')
  
  @app.route('/pong_new', methods=['POST'])
  def pong_new():
      name = request.form.get('name')
      msg = request.form.get('msg')
      return render_template('pong_new.html', name=name, msg=msg)
  ```

  - ping_new.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <h1>핑!</h1>
        <form action='/pong_new' method="POST">
            <input type="text" name="name"/>
            <input type="text" name="msg"/>
            <input type="submit" value="Submit"/>
        </form>
    </body>
    </html>
    ```

  - pong_new.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
        <h1>퐁!</h1>
        <h2>{{ name }}</h2>
        <h2>{{ msg }}</h2>
    </body>
    </html>
    ```

1.2. 위 코드는 post 방식으로 전달해줄 경우의 코드이다. 주요 차이점은 html에서 method=POST를 추가해줘야 한다. 그리고 앱 라우트에서도 코드를 추가 해줘야 하니 참고할것. 이 방식의 특징은 페이지 이동시에 주소창에 현재 내가 던져준 정보가 표시 되지 않는다.

## 2. timeline:timer_clock:

