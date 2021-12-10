require_relative "../board.rb"

board_input = "14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
2  0 12  3  7"

internal_board = [[14, 21, 17, 24, 4],
                [10, 16, 15, 9, 19],
                [18,  8, 23, 26, 20],
                [22, 11, 13, 6, 5],
                [2, 0, 12, 3, 7]]

empty_state = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]


RSpec.describe Board do
  context "Initialise" do
    it "Gives the correct representation of board" do
      board = Board.new(board_input)
      expect(board.Board).to eq(internal_board)
    end
  end
  context "Mark a number" do
    it "Gives the correct representation of board" do
      board = Board.new(board_input)
      board.mark_number(24)
      expect(board.state[0][3]).to eq(1)
    end
  end
  context "Check winning on rows" do
    it "Gives the correct representation of board" do
      board = Board.new(board_input)
      board.mark_number(24)
      board.mark_number(17)
      board.mark_number(21)
      board.mark_number(14)
      board.mark_number(4)
      expect(board.check_won?).to eq(true)
    end
  end
  context "Check winning on cols" do
    it "Gives the correct representation of board" do
      board = Board.new(board_input)
      board.mark_number(9)
      board.mark_number(3)
      board.mark_number(6)
      board.mark_number(24)
      board.mark_number(26)
      expect(board.check_won?).to eq(true)
    end
  end
  context "Check final value" do
    it "Gives the correct answer" do
      board = Board.new(board_input)
      board.mark_number(7)
      board.mark_number(4)
      board.mark_number(9)
      board.mark_number(5)
      board.mark_number(11)
      board.mark_number(17)
      board.mark_number(23)
      board.mark_number(2)
      board.mark_number(0)
      board.mark_number(14)
      board.mark_number(21)
      board.mark_number(24)
      expect(board.get_final_value(24)).to eq(4512)
    end
  end
end
