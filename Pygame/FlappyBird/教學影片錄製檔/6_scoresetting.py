'''
FlappyBird物件導向遊戲設計課程單元
教學製作：建國高中資訊科潘威歷老師
製作日期：2021/06/06
第六單元：分數物件基本設定
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
        self.jump=True
        self.jumpHeight = 10
        self.downHeight = 3 #按上鍵的話下降速度要重設

        
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
        if not self.dead: #如果還活著
            if self.jump: #按下上鍵時，Y座標往上位移
                self.jumpHeight = self.jumpHeight-1 #一直連按著會愈跳愈低
                self.Y -= self.jumpHeight #一直向上
            else:
                self.downHeight += 1 #往下愈來愈快
                self.Y += self.downHeight #一直向下
            
            self.status = (self.status+1)%3 #控制鳥的飛行動畫

    def CollisonDetect(self):
        '''
        用以處理碰撞偵測
        '''
        pass
        
    def RenderMap(self,scene):
        #將自己畫到遊戲畫面中
        scene.blit(self.birdimages[self.status],(self.X,self.Y))

class Pipe(object):
    def __init__(self):
        self.X=288 #因為遊戲畫面寬度只有288，所以預設在畫面外
        self.pipeUp = pygame.image.load('./img/pipe_up.png') #由下方往上延伸的水管圖形
        self.pipeDown = pygame.image.load('./img/pipe_down.png') #由上方往下延伸的水管圖形
        self.pipeUpY=362 #由下方往上延伸的水管圖形Y座標
        self.pipeDownY=-150 #由上方往下延伸的水管圖形Y座標
        #上下兩個水管的長方形碰撞偵測範圍
        self.rectUp = None
        self.rectDown = None
    def Move(self):
        self.X -= 2 #由右往左移動
        if self.X < -52: #若已移出左邊界，因為水管圖片的寬度為52，所以X座標移到-52表示整張圖都已經移出畫面之外了。
            self.X = 288 #則重設回右邊界之外再跑一次
            
    def GetRect(self):
        #將長方形碰撞偵測範圍回傳給鳥去偵測之用
        pass

    def GetX(self):
        '''
        回傳X座標給鳥，做為是否越過的判斷
        '''
        pass

    def RenderMap(self,scene):
        #將自己畫到遊戲畫面中
        scene.blit(self.pipeUp,(int(self.X),self.pipeUpY)) #這張是管子由下往上升出來的圖形，Y座標可以自己多試幾次找到合適的甜密點
        scene.blit(self.pipeDown,(int(self.X),self.pipeDownY))#這張是管子由上往下降下來的圖形，Y座標可以自己多試幾次找到合適的甜密點

class Score(object):
    '''
    專門處理畫面上分數計算之用
    '''
    def __init__(self):
        self.count=0
        self.font=pygame.font.Font('./font/NotoSansTC-Bold.otf',30)
        self.text=None
    def AddScore(self):
        '''
        每次越過水管可呼叫此方式加10分。
        '''
        self.count+=10

    def GetScore(self):
        '''
        想要知道目前累積分數可呼叫此方法。
        '''
        return self.count

    def RenderMap(self,scene):
        '''
        把自己畫到遊戲場景之中
        scene:遊戲場景物件
        '''
        #render(text, antialias, color, background=None) -> Surface
        self.text='目前分數:{}'.format(self.count)
        scene.blit(self.font.render(self.text,True,(255,255,255)),(70,20))
   
                               
if __name__=='__main__':
    pygame.init() #pygame初始化
    size=(288,512) #我們的背景圖是288*512，所以整個遊戲的大小我們就設定為288*512
    pygame.display.set_caption("FlappyBird建中潘威歷老師")
    scene=pygame.display.set_mode(size) #設定遊戲場景的大小，並回傳一個pygame.Surface物件。
    background = Background() #建立背景圖案物件。
    bird=Bird() #建立鳥物件。
    pipe=Pipe() #建立水管物件
    score=Score() #建立分數物件。
    clock=pygame.time.Clock() #建立計時器物件
    while True:
        clock.tick(30) #每1/30秒刷新畫面一次，相當於FPS=30。
        for event in pygame.event.get(): #從這段期間中使用者輸入的指令Queue（先進先出）中一個一個取出所有的指令比對。
            if event.type == pygame.QUIT: #如果是按下視窗中的'X'按鈕
                sys.exit() #則結束遊戲。
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird.Jump()

        background.RenderMap(scene) #繪製上背景圖
        pipe.Move()
        pipe.RenderMap(scene) #繪製上水管
        bird.Move()
        score.RenderMap(scene) #繪製上分數
        bird.RenderMap(scene) #繪製上鳥                                
        pygame.display.update() #遊戲畫面更新
        
    pygame.quit() #離開遊戲