state = 

class Piece():
    def __init__(self, color, x: int, y: int):
        self.color = color
        self.x = x
        self.y = y
        
    def __del__():
        pass

    def get_color(self):
        return self.color
        
    
class Pawn(Piece):
    def legal_moves(self, Pieces):
        

        return moves

class Bishop(Piece):
    def legal_moves(self):
        moves = []
        for square in square_list:
            dist_x = self.x - square.getX()
            dist_y = self.y - square.getY()
            if abs(dist_x) == abs(dist_y):
                moves.append(square)
            
            piece_in_path = square.getPiece()
            if piece_in_path == None:
                moves.append(square)
            else:
                if piece_in_path.get_color() != self.color:
                    moves.append(square)

        return moves

class Rook(Piece):
    def legal_moves(self, square_list):
        moves = []
        for square in square_list:
            if square.getX() == self.x or square.getY() == self.y:
                moves.append(square)
            
            piece_in_path = square.getPiece()
            if piece_in_path == None:
                moves.append(square)
            else:
                if piece_in_path.get_color() != self.color:
                    moves.append(square)

        return moves

class Knight(Piece):
    def legal_moves():
        

        return moves

class Queen(Piece):
    def legal_moves():
        

        return moves

class King(Piece):
    def legal_moves():
        

        return moves