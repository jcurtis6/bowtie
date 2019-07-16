def setup(): #runs once
    size(512, 512)
    noStroke()
def draw():   #run multiple times
     if mousePressed:
         fill(18, 255, 65)
         rect(mouseX-50, mouseY-50, 100,100 )
     if keyPressed and key == 'c':
              background(200, 200, 200)
              
