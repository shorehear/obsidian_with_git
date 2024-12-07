Синхронизация заметок в Obsidian с Github
---
По запуску скрипта через каждые 30 минут будет происходить git commit, git push указанной директории
---
Как настроить:
1. В переменной obsidian_path определить путь до директории, в которой содержатся файлы обсидиана
2. Позаботьтесь об актуальности вашей системы и библиотек, используемых в скрипте:
```bash
sudo apt update && sudo apt upgrade
sudo apt install git -y
sudo apt install python3 python-pip -y
pip3 install psutil
```
3. Если git не настроен на ваш аккаунт в Github, не имеет необходимого репозитория - IDE выдаст ошибку. Следуйте инструкциям из консоли: вероятнее всего, нужно будет авторизироваться, синхронизировать названия директории, из которой пушится проект и репозитория, в который пушится проект

На случай, если IDE не справится с авторизацией:
```bash
git config --global user.name 'username'
git config --global user.email 'email.com'
```
Если не помогает, используйте ssh-ключ или авторизируйтесь токеном доступа.

4. При возникновении непредвиденных ошибок можно ознакомиться с содержимым /ваша_папка/logger.txt - файл заполняется каждую итерацию цикла текущей датой, статусом Obsidian (запущен/нет), статусом пуша и возникшей ошибкой

Хотите обновление пушей чаще/реже? Измените последнюю строку скрипта: *time.sleep(количество_секунд_до_следующего_пуша)*
