'''
FlappyBird物件導向遊戲設計課程單元
教學製作：建國高中資訊科潘威歷老師
製作日期：2021/06/06
第二單元：遊戲背景的基本設定
'''
import pygame,sys
class Background(object):
    def __init__(self):
        self.X = 0 #背景圖案的預設X座標
        self.Y = 0 #背景圖案的預設Y座標
        self.img=pygame.image.load('./img/bg_day.png') #背景圖案的Surface物件。
    def RenderResult(self):
        '''
        用來處理遊戲結束時的畫面。
        '''
        pass
        
    def RenderMap(self,scene):
        '''
        將鳥畫到遊戲畫面中
        screen:遊戲場景物件
        '''        
        scene.blit(self.img,(self.X,self.Y))

if __name__=='__main__':
    pygame.init() #pygame初始化
    size=(288,512) #我們的背景圖是288*512，所以整個遊戲的大小我們就設定為288*512
    pygame.display.set_caption("FlappyBird建中潘威歷老師")
    gamescene=pygame.display.set_mode(size) #設定遊戲場景的大小，並回傳一個pygame.Surface物件。
    background = Background() #建立背景圖案物件。
    
    clock=pygame.time.Clock() #建立計時器物件
    while True:
        clock.tick(30) #每1/30秒刷新畫面一次，相當於FPS=30。
        for event in pygame.event.get(): #從這段期間中使用者輸入的指令Queue（先進先出）中一個一個取出所有的指令比對。
            if event.type == pygame.QUIT: #如果是按下視窗中的'X'按鈕
                sys.exit() #則結束遊戲。
        background.RenderMap(gamescene) #繪製上背景圖                                
        pygame.display.update() #遊戲畫面更新
        
    pygame.quit() #離開遊戲