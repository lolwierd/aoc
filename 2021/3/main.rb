def take_input
  File.read("input.txt").split
end

def get_all_of_index(numbers, index)
  numbers.map {|number| number[index]}
end

def get_most_least_common_of_index(numbers, index)
  num_1 = 0
  all_of_index = get_all_of_index(numbers, index)
  all_of_index.each do |number|
    if number == "1"
      num_1 += 1
    end
  end
  num_1 > all_of_index.length / 2 ? ["1", "0"] : ["0", "1"]
end

def sol_1(numbers)
  total_indices = numbers[0].length
  gamma_rate = ""
  epsilon_rate = ""
  (0..total_indices-1).each do |index|
    gamma, epsilon = get_most_least_common_of_index numbers, index
    gamma_rate << gamma
    epsilon_rate << epsilon
  end
  gamma_rate.to_i(2) * epsilon_rate.to_i(2)
end

def sol_2(numbers)
  raise "TODO!!"
end

def main
  numbers = take_input
  puts sol_1(numbers)
  puts sol_2(numbers)
end

main