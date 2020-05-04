from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.urls import reverse
from django.views import View

from .forms import LoginForm


class LoginView(View):
    def get(self, request, *args, **kwargs):
        """GETリクエスト用のメソッド"""
        context = {
            'form': LoginForm(),
        }
        # ログイン画面用のテンプレートに値が空のフォームをレンダリング
        return render(request, 'accounts/login.html', context)

    def post(self, request, *args, **kwargs):
        """POSTリクエスト用のメソッド"""
        # リクエストからフォームを作成
        form = LoginForm(request.POST)
        # バリデーション（ユーザーの認証を合わせて実施）
        if not form.is_valid():
            # バリデーションNGの場合はログイン画面のテンプレートを再表示
            return render(request, 'accounts/login.html', {'form': form})
        # User オブジェクトをフォームから取得
        user = form.get_user()

        # ログイン処理(取得したUserオブジェクトをセッションに保存＆Userデータを更新)
        auth_login(request, user)
        # ログイン画面用のテンプレートに値がからのフォームをレンダリング
        return redirect(reverse('shop:index'))


login = LoginView.as_view()
