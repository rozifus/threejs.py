import math
import Vector3

class Ray: 

    def __init__( self, 
                  origin      =   Vector3(), 
                  direction   =   Vector3(), 
                  near        =   float(0), 
                  far         =   float("inf") 
                  ):

        self.origin     =   origin
        self.direction  =   direction
        self.near       =   near
        self.far        =   far

        self.originCopy         =   Vector3()
        self.localOriginCopy    =   Vector3()
        self.localDirectionCopy =   Vector3()

        self.vector             =   Vector3()
        self.normal             =   Vector3()
        self.intersectPoint     =   Vector3()

        self.inverseMatrix      =   Matrix4()

        self.v0 = Vector3()
        self.v1 = Vector3()
        self.v2 = Vector3()

    def descSort( a, b ):

        return a.distance - b.distance

    def distanceFromIntersection( origin, direction, position ):

        v0.sub( position, origin )

        dot = v0.dot( direction )
        
        intersect = v1.add( origin, 
                            v2.copy( direction ).multiplyScalar( dot ) )
        distance = position.distanceTo( intersect )

        return distance

    def pointInFace3 ( p, a, b, c ):
        v0.sub( c, a )
        v1.sub( b, a )
        v2.sub( p, a )

        dot00 = v0.dot( v0 )
        dot01 = v0.dot( v1 )
        dot02 = v0.dot( v2 )
        dot11 = v1.dot( v1 )
        dot12 = v1.dot( v2 )

        invDenom = 1 / ( dot00 * dot11 - dot01 * dot01 )
        u = ( dot11 * dot02 - dot01 * dot12 ) * invDenom
        v = ( dot00 * dot12 - dot01 * dot02 ) * invDenom

        return ( u >= 0 ) and ( v >= 0 ) and ( u + v < 1 )
