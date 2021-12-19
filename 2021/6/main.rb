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
  # File.read(is_trial ? "trial.txt" : "input.txt").split(',').map {|timer| LanternFish.new(timer.to_i)}
  File.read(is_trial ? "trial.txt" : "input.txt").split(',')
end

def sol_1(hash)
  # (1..80).each do 
  #   system.simulate
  # end
  # system.get_lanternfish_number
  (1..80).each do |i|
    temp = hash["1"]
    (1..7).each do |j|
      hash[j.to_s] = hash[(j+1).to_s]
    end
    hash["6"] += hash["0"]
    hash["8"] = hash["0"]
    hash["0"] = temp
  end
  num_fish = 0
  hash.each do |key, value|
    num_fish += value
  end
  num_fish
end

def sol_2(hash)
  (1..256).each do |i|
    temp = hash["1"]
    (1..7).each do |j|
      hash[j.to_s] = hash[(j+1).to_s]
    end
    hash["6"] += hash["0"]
    hash["8"] = hash["0"]
    hash["0"] = temp
  end
  num_fish = 0
  hash.each do |key, value|
    num_fish += value
  end
  num_fish
end

def main
  fishes = take_input
  hash = {"0" => 0, "1" => 0, "2" => 0, "3" => 0, "4" => 0, "5" => 0, "6" => 0, "7" => 0, "8" => 0}
  fishes.each do |fish|
    hash[fish] += 1
  end

  puts sol_1(hash.clone)
  puts sol_2(hash.clone)
end

main