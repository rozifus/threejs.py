import math

class Vector2:

    def __init__( self, x=0, y=0 ):

        self.x = x
        self.y = y

    def set( x, y ):

        self.x = x
        self.y = y

        return self

    def copy( v ):

        self.x = v.x
        self.y = v.y

        return self

    def add( a, b ):

        self.x = a.x + b.x
        self.y = a.y + b.y

        return self

    def addSelf( v ): 

        self.x += v.x
        self.y += v.y

        return self

    def sub( a, b ):

        self.x = a.x - b.x
        self.y = a.y - b.y

        return self

    def subSelf( v ):

        self.x -= v.x
        self.y -= v.y

        return self

    def multiplyScalar( s ):

        self.x *= s
        self.y *= s

        return self

    def divideScalar( s ):

        if s:
            self.x /= s
            self.y /= s
        else: 
            self.set(0,0)

        return self 

    def negate():

        return self.multiplyScalar(-1)

    def dot( v ):

        return self.x * v.x + self.y * v.y

    def lengthSq():

        return self.x * self.x + self.y * self.y

    def length():

        return math.sqrt( self.lengthSq() )

    def normalize():

        return self.divideScalar( self.length() )

    def distanceTo( v ):

        return math.sqrt( self.distanceToSquared( v ) ) 

    def distanceToSquared( v ):
        
        dx = self.x - v.x
        dy = self.y - v.y

        return dx * dx + dy * dy

    def setLength( l ):

        return self.normalize().multiplyScalar( l )

    def lerpSelf( v, alpha ):

        self.x += ( v.x - self.x ) * alpha
        self.y += ( v.y - self.y ) * alpha

    def equals( v ):

        return ( ( v.x == self.x ) and ( v.y == self.y ) )

    def isZero( v=0.0001 ):

        return self.lengthSq() < v  

    def clone:

        return Vector2( self.x, self.y )
    
