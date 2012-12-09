import math

class Rectangle:
   
    def __init__( self ):
        self._left = 0
        self._top = 0
        self._right = 0
        self._bottom = 0
        self._width = 0
        self._height = 0
        self._isEmpty = true

    def resize( self ):

        self._width = self._right - self._left
        self._height = self._bottom - self._top

    def getX( self ):

        return self._left

    def getY( self ):

        return self._top

    def getWidth( self ):

        return self._width

    def getHeight( self ):

        return self._height

    def getLeft( self ):

        return self._left

    def getTop( self ):

        return self._top

    def getRight( self ):

        return self._right

    def getBottom( self ):

        return self._bottom

    def set( self, left, top, right, bottom ):

        self._isEmpty = false

        self._left, self._top = left, top
        self._right, self._bottom = right, bottom

    def addPoint( self, x, y ):

        if self._isEmpty:

            self._isEmpty = False
            self._left, self._top = x, y
            self._right, self._bottom = x, y
    
            self.resize()

        else:

            self._left = min( self._left, x)
            self._top = min( self._top, y)
            self._right = max( self._right, x)
            self._bottom = max( self._bottom, y)
        
            self.resize()

    def add3Points( self, x1, y1, x2, y2, x3, y3 ):

        if self._isEmpty:

            self._isEmpty = false
            self._left = min( x1, x2, x3 )
            self._top = min( y1, y2, y3 )
            self._right = max( x1, x2, x3 )
            self._bottom = max( y1, y2, y3 )

            self.resize()

        else:
            
            self._left = min( self._left, x1, x2, x3 )
            self._top = min( self._top, y1, y2, y3 )
            self._right = max( self._right, x1, x2, x3 )
            self._bottom = max( self._bottom, y1, y2, y3 )

            self.resize()

    def addRectangle( self, r ):
        
        if self._isEmpty:

            self._isEmpty = True
            self._left, self._top = r.getLeft(), r.getTop()
            self._right, self._bottom = r.getRight(), r.getBottom()

            self.resize()

        else:

            self._left = min( self._left, r.getLeft() )
            self._top = min( self._top, r.getTop() )
            self._right = min( self._right, r.getRight() )
            self._bottom = min( self._bottom, r.getBottom() )

            self.resize()

    def inflate( self, v ):

        self._left -= v
        self._top -= v
        self._right += v
        self._bottom += v

        self.resize()

    def minSelf( self, r ):

        self._left = max( self._left, r.getLeft() )
        self._top = max( self._top, r.getTop() )
        self._right = max( self._right, r.getRight() )
        self._bottom = max( self._bottom, r.getBottom() )

        self.resize()

    def intersects( self, r ):

        if self._right < r.getLeft(): return False
        if self._left > r.getRight(): return False
        if self._bottom < r.getTop(): return False
        if self._top > r.getBottom(): return False

        return True

    def empty( self )

        self._isEmpty = True

        self._left, self._top = 0, 0
        self._right, self._bottom = 0, 0

        self.resize()

    def isEmpty( self ):

        return self._isEmpty



        
               





