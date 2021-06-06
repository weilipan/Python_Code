'''
FlappyBird物件導向遊戲設計課程單元
教學製作：建國高中資訊科潘威歷老師
製作日期：2021/06/04
第一單元：遊戲場景的設定
'''
import pygame,sys

if __name__=='__main__':
    pygame.init() #pygame初始化
    size=(288,512) #我們的背景圖是288*512，所以整個遊戲的大小我們就設定為288*512
    pygame.display.set_caption("FlappyBird建中潘威歷老師")
    gamescene=pygame.display.set_mode(size) #設定遊戲場景的大小，並回傳一個pygame.Surface物件。
    
    clock=pygame.time.Clock() #建立計時器物件
    while True:
        clock.tick(30) #每1/30秒刷新畫面一次，相當於FPS=30。
        for event in pygame.event.get(): #從這段期間中使用者輸入的指令Queue（先進先出）中一個一個取出所有的指令比對。
            if event.type == pygame.QUIT: #如果是按下視窗中的'X'按鈕
                sys.exit() #則結束遊戲。
                                
        pygame.display.update() #遊戲畫面更新
        
    pygame.quit() #離開遊戲