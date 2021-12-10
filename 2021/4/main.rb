=begin
Board Representation

2 arrays one board and one status -  5X5 grid
status of 0 denotes unmarked and status of 1 denotes marked
=end

require_relative "bingo"

def take_input
  File.read('input.txt').split("\n\n")
end

def sol(puzzle_input, boards, get_final)
  bingo = Bingo.new(boards)
  puzzle_input.each do |number|
   final_score = get_final ? bingo.play_for_last_win(number) : bingo.play(number) 
   if final_score
    return final_score
   end
  end
  raise "No board Completed?!?!!?"
end

def main
  puzzle_input, *boards = take_input
  puts sol(puzzle_input.split(",").map(&:to_i), boards, false)
  puts sol(puzzle_input.split(",").map(&:to_i), boards, true)
end

main