class LanternFish
  def initialize(timer)
    @internal_timer = timer
  end
  
  def simulate
    if @internal_timer == 0
      @internal_timer = 6
      LanternFish.new(8)
    else
      @internal_timer -= 1
      nil
    end
  end
end

class System

  def initialize(lanternfishes)
    @lanternfishes = lanternfishes
  end
  # Instead of dealing with one large array, deal with multiple smaller arrays concurrently
  def simulate 
    to_add = []
    @lanternfishes.each do |lanternfish|
      result = lanternfish.simulate
      if result
        to_add << result
      end
    end
    @lanternfishes += to_add
  end

  def get_lanternfish_number
    @lanternfishes.length
  end
end

def take_input(is_trial = false)
  File.read(is_trial ? "trial.txt" : "input.txt").split(',').map {|timer| LanternFish.new(timer.to_i)}
end

def sol_1(system)
  (1..80).each do 
    system.simulate
  end
  system.get_lanternfish_number
end

def sol_2(system)
  (1..256).each do |num|
    puts "Simulating Day: #{num}"
    system.simulate
  end
  system.get_lanternfish_number
end

def main
  fishes = take_input
  puts sol_1(System.new(fishes))
  puts sol_2(System.new(fishes))
end

main