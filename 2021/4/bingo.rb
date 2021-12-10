require_relative "board.rb"

class Bingo
  attr_reader :boards

  def initialize(boards)
    @boards = boards.map { |board| Board.new(board) }
  end

  def play(number)
    @boards.each do |board|
      board.mark_number number
      if board.check_won?
        return board.get_final_value number
      end
    end
    nil
  end

  def play_for_last_win(number)
    @boards.each do |board|
      board.mark_number number
      if board.check_won?
        if @boards.length == 1
          return board.get_final_value number
        else
          @boards = @boards - [board]
        end
      end
    end
    nil
  end
end
