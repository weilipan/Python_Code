'''
FlappyBird物件導向遊戲設計課程單元
教學製作：建國高中資訊科潘威歷老師
製作日期：2021/06/06
第十單元：只是加上擷取遊戲畫面的功能
'''
import pygame,sys,datetime
class Background(object):
    def __init__(self):
        self.X = 0 #背景圖案的預設X座標
        self.Y = 0 #背景圖案的預設Y座標
        self.img=pygame.image.load('./img/bg_day.png') #背景圖案的Surface物件。
    def RenderResult(self,scene,bird,score):
        '''
        用來處理遊戲結束時的畫面。
        '''
        text1 = '遊戲結束' #顯示Game Over字樣
        text2 = '最終分數為 {} 分'.format(score.GetScore()) #顯示遊戲結束時的總分
        fontText1 = pygame.font.Font('./font/NotoSansTC-Bold.otf', 25) #第一行字的大小，如果要用電腦內已安裝好的字型，請用pygame.font.SysFont
        fontText2 = pygame.font.Font('./font/NotoSansTC-Bold.otf', 25) #第二行字的大小
        renderText1 = fontText1.render(text1,1,(242,3,36)) #設定文字及顏色
        renderText2 = fontText2.render(text2,1,(253,177,6)) #設定文字及顏色
        scene.blit(bird.birdimages[bird.status],(bird.X,bird.Y)) #顯示鳥死亡的圖形
        scene.blit(renderText1,[100,100]) #呈現在遊戲畫面之上
        scene.blit(renderText2,[60,150]) #呈現在遊戲畫面之上

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

        
    def ScoreCount(self,pipe,score):
        '''
        用以處理分數計算，只要flappybird順利越過水管則加10分
        '''
        if self.X==pipe.GetX(): #若鳥已越過水管
            score.AddScore() #呼叫score的AddScore()方法，讓總分加10分。
 
        
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

    def CollisonDetect(self,pipe):
        '''
        用以處理碰撞偵測
        '''
        (rectUp,rectDown)=pipe.GetRect() #取得水管的長方形範圍
        self.rect = pygame.Rect(self.X,self.Y,self.birdimages[1].get_width(),self.birdimages[1].get_height())
        if self.rect.colliderect(rectUp) or self.rect.colliderect(rectDown) or (not 0 < self.rect[1] < 464):
            #整張背景的高度為512，鳥的高度為48，所以鳥必須在要0~464(512-48)的範圍移動，否則碰到上下邊界就算死亡
            self.dead = True #設定為鳥死
            self.status = 3 #鳥死掉的圖形對應到索引值3的圖
        return self.dead #回傳鳥的死活狀態，用以判斷是不是要繼續遊戲
        
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
        self.rectUp = pygame.Rect(self.X,362,self.pipeUp.get_width(),self.pipeUp.get_height())
        self.rectDown = pygame.Rect(self.X,-150,self.pipeDown.get_width(),self.pipeDown.get_height())
        return (self.rectUp,self.rectDown) #因為有上下兩根水管，所以回傳一對tuple


    def GetX(self):
        '''
        回傳X座標給鳥，做為是否越過的判斷
        '''
        return self.X+self.pipeDown.get_width()

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
                if event.key == pygame.K_s: #如果按下s鍵，則將畫面截圖存放於cap資料夾中
                    pygame.image.save(scene, './cap/'+str(datetime.datetime.now().timestamp())+'.png')

        if bird.CollisonDetect(pipe): #偵測碰撞情形
             background.RenderResult(scene,bird,score)
        else:
            background.RenderMap(scene) #繪製上背景圖
            pipe.Move()
            pipe.RenderMap(scene) #繪製上水管
            bird.Move()
            bird.ScoreCount(pipe,score) #計算分數
            score.RenderMap(scene) #繪製上分數
            bird.RenderMap(scene) #繪製上鳥                                
        
        pygame.display.update() #遊戲畫面更新
        
    pygame.quit() #離開遊戲