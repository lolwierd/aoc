class Command
  attr_reader :direction, :magnitude

  def initialize(command)
    @direction = command.split.[] 0
    @magnitude = command.split[1].to_i
  end
end

def take_input
  File.read("input.txt").split("\n").map! {|element| Command.new(element)}
end

def sol_1(commands)
  horizontal = 0
  depth = 0
  commands.each do |command|
    case command.direction
    when "forward"
      horizontal += command.magnitude
    when "up"
      depth -= command.magnitude
    when "down"
      depth += command.magnitude
    end
  end
  horizontal*depth
end

def sol_2(commands)
  horizontal = 0
  depth = 0
  aim = 0
  commands.each do |command|
    case command.direction
    when "forward"
      horizontal += command.magnitude
      depth += aim * command.magnitude
    when "up"
      aim -= command.magnitude
    when "down"
      aim += command.magnitude
    end
  end
  horizontal*depth
end

def main
  commands = take_input
  puts sol_1(commands)
  puts sol_2(commands)
end

main