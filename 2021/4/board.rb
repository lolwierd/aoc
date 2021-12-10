class Board
  attr_reader :Board, :state

  def initialize(board)
    @state = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]
    @Board = board.split("\n").map do |row|
      row.split.map(&:to_i)
    end
  end

  def mark_number(number)
    row, col = self.check_number(number)
    if row!=nil && col != nil
      @state[row][col] = 1
    end
  end


  def get_final_value(last_marked_number)
    unmarked_sum = 0
    @Board.each_with_index do |row, row_idx|
      row.each_with_index do |number, col_idx|
        if state[row_idx][col_idx] == 0
          unmarked_sum += @Board[row_idx][col_idx]
        end
      end
    end
    unmarked_sum * last_marked_number
  end

  def check_won?
    check_rows? || check_cols?
  end

  # private

  def check_rows?
    state.each do |row|
      if row.sum == 5
        return true
      end
    end
    false
  end

  def check_cols?
    5.times do |col|
      sum = 0
      5.times do |row|
        sum += state[row][col]
      end
      if sum == 5
        return true
      end
    end
    false
  end

  def check_number(number_to_check)
    @Board.each_with_index do |row, row_num|
      row.each_with_index do |number, col_num|
        if number_to_check == number
          return [row_num, col_num]
        end
      end
    end
    return []
  end
end