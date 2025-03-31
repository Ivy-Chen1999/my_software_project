classDiagram
    class MonopolyGame {
        -startSquare: Square
        -jailSquare: Square
    }

    class Dice
    class GameBoard
    class Square
    class Token
    class Player {
        -money: int
    }

    class Card {
        +executeAction()
    }

    class Action

    class Street {
        -name: string
        -numHouses: int
        -hasHotel: bool
        -owner: Player
    }

    class Station
    class Utility
    class ChanceSquare
    class CommunityChestSquare
    class StartSquare
    class JailSquare

    %% Basic associations
    MonopolyGame "1" -- "2" Dice
    MonopolyGame "1" -- "1" GameBoard
    Player "2..8" -- "1" MonopolyGame
    Token "1" -- "1" Player
    Square "1" -- "0..8" Token
    GameBoard "1" -- "40" Square
    Square "1" --> "1" Square : next

    %% Square types (inheritance)
    Street --|> Square
    Station --|> Square
    Utility --|> Square
    ChanceSquare --|> Square
    CommunityChestSquare --|> Square
    StartSquare --|> Square
    JailSquare --|> Square

    %% Cards and actions
    Card --> Action
    ChanceSquare "0..*" --> "1..*" Card
    CommunityChestSquare "0..*" --> "1..*" Card

    Street --> Player : owner
