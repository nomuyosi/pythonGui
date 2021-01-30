
#参考：https://qiita.com/Tomo666/items/1b64aa91dcd45ad91540

# モジュールのインポート
import os, tkinter, tkinter.filedialog, tkinter.messagebox

def py_gui_file():
    # ファイル選択ダイアログの表示
    root = tkinter.Tk()
    root.withdraw()

    fTyp = [("","*")]
    # 拡張子指定の場合ここの1行を変更
    #fTyp = [("","*.csv")]

    iDir = os.path.abspath(os.path.dirname(__file__))
    tkinter.messagebox.showinfo('ファイル選択','処理ファイルを選択してください！')

    # ここの1行を変更 askopenfilename → askopenfilenames
    file = tkinter.filedialog.askopenfilenames(filetypes = fTyp,initialdir = iDir)

    # 選択ファイルリスト作成
    list_select_file = list(file)
    tkinter.messagebox.showinfo('ファイル選択',list_select_file)
    return list_select_file