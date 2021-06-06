'''
FlappyBird物件導向遊戲設計課程單元
教學製作：建國高中資訊科潘威歷老師
製作日期：2021/06/06
第三單元：鳥物件基本設定
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
        
class Bird(object):
    def __init__(self):
        # 有關Bird的相關圖檔集，建立圖案陣列
        self.birdimages=[
            pygame.image.load('./img/bird0_0.png'),
            pygame.image.load('./img/bird0_1.png'),
            pygame.image.load('./img/bird0_2.png'),
            pygame.image.load('./img/dead.png')
        ]
        self.status = 0 #預設為第一張圖。
        self.X = 50 #預設的X座標。
        self.Y = 250 #預設的Y座標。
        self.jump = False #預設是向下移動，除非使用者按上鍵造成跳躍效果。
        self.jumpHeight = 10 #預設跳起來的高度，向上移動的量。
        self.downHeight = 3 #預設向下移動的量。
        self.dead = False #預設活著。
        #建立flappy bird的碰撞偵測長方形
        self.rect = pygame.Rect(self.X,self.Y,self.birdimages[1].get_width(),self.birdimages[1].get_height())
    
    def Jump(self):
        '''
        當玩家按下「↑」鍵時，鳥應該做的動作
        '''
        pass
        
    def ScoreCount(self):
        '''
        用以處理分數計算，只要flappybird順利越過水管則加10分
        '''
        pass
        
    def Move(self):
        '''
        控制鳥類移動
        '''
        '''
        讓翅膀會動，因為self.birdimages=[
            pygame.image.load('./img/bird0_0.png'),
            pygame.image.load('./img/bird0_1.png'),
            pygame.image.load('./img/bird0_2.png'),
            pygame.image.load('./img/dead.png')
        ]
        前三張是連續拍翅膀的圖，所以mod3。
        '''    
        pass

    def CollisonDetect(self):
        '''
        用以處理碰撞偵測
        '''
        pass
        
    def RenderMap(self,scene):
        #將自己畫到遊戲畫面中
        scene.blit(self.birdimages[self.status],(self.X,self.Y))
                                
if __name__=='__main__':
    pygame.init() #pygame初始化
    size=(288,512) #我們的背景圖是288*512，所以整個遊戲的大小我們就設定為288*512
    pygame.display.set_caption("FlappyBird建中潘威歷老師")
    scene=pygame.display.set_mode(size) #設定遊戲場景的大小，並回傳一個pygame.Surface物件。
    background = Background() #建立背景圖案物件。
    bird=Bird() #建立鳥物件。
    clock=pygame.time.Clock() #建立計時器物件
    while True:
        clock.tick(30) #每1/30秒刷新畫面一次，相當於FPS=30。
        for event in pygame.event.get(): #從這段期間中使用者輸入的指令Queue（先進先出）中一個一個取出所有的指令比對。
            if event.type == pygame.QUIT: #如果是按下視窗中的'X'按鈕
                sys.exit() #則結束遊戲。
        background.RenderMap(scene) #繪製上背景圖
        bird.RenderMap(scene) #繪製上鳥                                
        pygame.display.update() #遊戲畫面更新
        
    pygame.quit() #離開遊戲