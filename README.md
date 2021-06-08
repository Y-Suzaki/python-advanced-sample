# IntelliJにPythonのLinterとFormatterを導入
## 事前準備
1. IntelliJのPluginに、File Watcherを追加する。

## flake8
静的解析を行うライブラリ。
* install
    ```
    pip install flake8
    ```
* IntelliJの設定（File Watcherの設定を追加）
    * Name：flake8
    * File Type：Python
    * Program： （flake8へのパスを通す。）
    * Arguments：$FilePath$ --config=$ProjectFileDir$\.flake8
    * Advance Options
        * Auto-save edited files to trigger the watcher：OFF

## autopep8
改行やブランクなど、PEP8に従ってフォーマットしてくれるライブラリ。
* install
    ```
    pip install autopep8
    ```
* IntelliJの設定（File Watcherの設定を追加）
    * Name：autopep8
    * File Type：Python
    * Program： （autopep8へのパスを通す。）
    * Arguments：$FilePath$ --in-place --aggressive --aggressive --global-config $ProjectFileDir$/.flake8
    * Advance Options
        * Auto-save edited files to trigger the watcher：OFF

## isort
import文をソートしてくれるライブラリ。
* install
    ```
    pip install isort
    ```
* IntelliJの設定（File Watcherの設定を追加）
    * Name：isort
    * File Type：Python
    * Program： （isortへのパスを通す。）
    * Arguments：$FilePath$
    * Advance Options
        * Auto-save edited files to trigger the watcher：OFF