import tkinter as tk

class FolderPanel:
    def __init__(self, window, BtnFont, EntryFont):
        self.OutputText = tk.Label(window, text ="請選擇輸出方式", font = BtnFont)
        self.ActiveText = tk.Label(window, text ="請勾選要處理的檔案", font = EntryFont)
        self.OutputPlace = tk.Button(window, text ="選擇輸出資料夾", bg = "light blue", width = '15', height = '1', font = EntryFont)
        self.FolderBtn = tk.Button(window, text ="選擇資料夾", bg = "light blue", width = '10', height = '1', font = BtnFont)
        self.WillCover = tk.BooleanVar()
        self.WillCover_Btn = tk.Checkbutton(window, text='直接覆蓋原檔案', var = self.WillCover, font = EntryFont)
        self.ActiveAss = tk.BooleanVar()
        self.ActiveAss_Btn = tk.Checkbutton(window, text='轉換.ass檔案', var = self.ActiveAss, font = EntryFont)
        self.ActiveLrc = tk.BooleanVar()
        self.ActiveLrc_Btn = tk.Checkbutton(window, text='轉換.lrc檔案', var = self.ActiveLrc, font = EntryFont)
        self.ActiveTxt = tk.BooleanVar()
        self.ActiveTxt_Btn = tk.Checkbutton(window, text='轉換.txt檔案', var = self.ActiveTxt, font = EntryFont)
        self.ActiveSrt = tk.BooleanVar()
        self.ActiveSrt_Btn = tk.Checkbutton(window, text='轉換.srt檔案', var = self.ActiveSrt, font = EntryFont)
        ##
        self.WillCover_Btn.config(command = lambda:self.CoverEvent())

    def ShowUI(self):
        self.OutputText.place(x = 400, y = 150)
        self.ActiveText.place(x = 600, y = 100)
        self.FolderBtn.place(x = 400, y = 50)
        self.WillCover_Btn.place(x = 400, y = 200)
        self.ActiveAss_Btn.place(x = 800, y = 25)
        self.ActiveLrc_Btn.place(x = 800, y = 75)
        self.ActiveTxt_Btn.place(x = 800, y = 125)
        self.ActiveSrt_Btn.place(x = 800, y = 175)
        self.CoverEvent()

    def HideUI(self):
        self.OutputText.place_forget()
        self.ActiveText.place_forget()
        self.OutputPlace.place_forget()
        self.FolderBtn.place_forget()
        self.WillCover_Btn.place_forget()
        self.ActiveAss_Btn.place_forget()
        self.ActiveLrc_Btn.place_forget()
        self.ActiveTxt_Btn.place_forget()
        self.ActiveSrt_Btn.place_forget()
    
    def CoverEvent(self):
        if self.WillCover.get() :
            self.OutputPlace.place_forget()
        else :
            self.OutputPlace.place(x = 400, y = 250)