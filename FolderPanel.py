import tkinter as tk
from tkinter import filedialog
from zhconv import convert
from ConvertEvent import *
from ReadEvent import *
import os

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
        self.ExecuteBtn = tk.Button(window, text='開始轉換', bg = "light blue", font = BtnFont)
        ##
        self.ToSim = tk.BooleanVar()
        self.ToSim_Btn = tk.Checkbutton(window, text='轉換成簡體字', var = self.ToSim, font = EntryFont)
        self.ToTrd = tk.BooleanVar()
        self.ToTrd_Btn = tk.Checkbutton(window, text='轉換成繁體字', var = self.ToTrd, font = EntryFont)
        ##
        self.FolderText = tk.Label(window, text ="", font = EntryFont)
        self.OutputFText = tk.Label(window, text ="", font = EntryFont)
        self.StatusText = tk.Label(window, text ="", font = EntryFont)
        ##
        self.filelist = []
        self.Pathreg = ""
        self.Outputreg = ""
        self.Coverreg = False
        self.STreg = ""
        ##
        self.WillCover_Btn.config(command = lambda:self.CoverEvent())
        self.FolderBtn.config(command = lambda:self.ChooseFolder())
        self.ExecuteBtn.config(command = lambda:self.ConvertAction())
        self.OutputPlace.config(command = lambda:self.ChooseOutput())
        self.ToTrd_Btn.config(command = lambda:self.ChooseTrd())
        self.ToSim_Btn.config(command = lambda:self.ChooseSim())

    def ShowUI(self):
        self.OutputText.place(x = 400, y = 150)
        self.ActiveText.place(x = 220, y = 25)
        self.FolderBtn.place(x = 400, y = 50)
        self.WillCover_Btn.place(x = 400, y = 200)
        self.ActiveAss_Btn.place(x = 220, y = 70)
        self.ActiveLrc_Btn.place(x = 220, y = 120)
        self.ActiveTxt_Btn.place(x = 220, y = 170)
        self.ActiveSrt_Btn.place(x = 220, y = 220)
        self.ExecuteBtn.place(x = 400, y = 325)
        self.FolderText.place(x = 600, y = 62)
        self.ToSim_Btn.place(x = 220, y = 340)
        self.ToTrd_Btn.place(x = 220, y = 290)
        self.StatusText.place(x = 550, y = 325)
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
        self.FolderText.place_forget()
        self.OutputFText.place_forget()
        self.ToSim_Btn.place_forget()
        self.ToTrd_Btn.place_forget()
        self.StatusText.place_forget()
        self.ExecuteBtn.place_forget()
        
    def CoverEvent(self):
        if self.WillCover.get() :
            self.OutputPlace.place_forget()
            self.OutputFText.place_forget()
            self.Coverreg = True
        else :
            self.OutputPlace.place(x = 400, y = 250)
            self.OutputFText.place(x = 600, y = 253)
            self.Coverreg = False

    def ChooseFolder(self):
        file_path = filedialog.askdirectory()
        if file_path != "":
            self.FolderText.config(text = file_path)
            self.Pathreg = file_path
            self.StatusText.config(text = "")

    def ChooseOutput(self):
        self.Outputreg = filedialog.askdirectory()
        if self.Outputreg != "":
            self.OutputFText.config(text = self.Outputreg)
    
    def ConvertAction(self):
        self.filelist = []
        if self.Pathreg == "" :
            self.StatusText.config(text = "請選擇欲轉換的資料夾！")
            return
        if not self.Coverreg and self.Outputreg == "":
            self.StatusText.config(text = "請選擇輸出資料夾！")
            return
        if self.STreg == "":
            self.StatusText.config(text = "請選擇輸出語言！")
            return
        for root, dirs, files in os.walk(self.Pathreg):
            for file in files:
                if self.ActiveAss.get() and os.path.splitext(file)[1] == '.ass' :
                    self.filelist.append(os.path.join(root, file))
                if self.ActiveLrc.get() and os.path.splitext(file)[1] == '.lrc' :
                    self.filelist.append(os.path.join(root, file))
                if self.ActiveTxt.get() and os.path.splitext(file)[1] == '.txt' :
                    self.filelist.append(os.path.join(root, file))
                if self.ActiveSrt.get() and os.path.splitext(file)[1] == '.srt' :
                    self.filelist.append(os.path.join(root, file))
        if len(self.filelist) == 0 :
            self.StatusText.config(text = "沒有對應檔案")
            return
        for file in self.filelist :
            if os.path.splitext(file)[1] == '.ass' :
                lines = ReadData(file)
                ConvertData = ConvertAss(lines, self.STreg)
            else :
                lines = ReadData(file)
                ConvertData = Convert(lines, self.STreg)
            if self.Coverreg :
                status = Output_Cover(ConvertData, file)
            else :
                status = Output_NoCover(ConvertData, file, self.Outputreg)
            if not status:
                break
        if status:
            self.Initial()
            self.StatusText.config(text = "轉換完成")
        else :
            self.StatusText.config(text = "轉換錯誤")
    
    def Initial(self):
        self.FolderText.config(text = "")
        self.OutputFText.config(text = "")
        self.Pathreg = ""
        self.Outputreg = ""

    def ChooseSim(self):
        if self.ToSim.get() :
            self.ToTrd.set(False)
            self.STreg = "zh-cn"
    
    def ChooseTrd(self):
        if self.ToTrd.get() :
            self.ToSim.set(False)
            self.STreg = "zh-tw"
