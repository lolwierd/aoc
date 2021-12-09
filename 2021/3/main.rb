def take_input
  File.read("input.txt").split
end

def get_all_of_index(numbers, index)
  numbers.map {|number| number[index]}
end

def get_least_most_common_of_index(numbers, index)
  if index > numbers[0].length-1
    raise "WTF r u doin?"
  end
  num_1 = 0
  all_of_index = get_all_of_index(numbers, index)
  all_of_index.each do |number|
    if number == "1"
      num_1 += 1
    end
  end
  num_1 > all_of_index.length / 2 ? ["0", "1"] : ["1", "0"]
end

def sol_1(numbers)
  total_indices = numbers[0].length
  gamma_rate = ""
  epsilon_rate = ""
  (0..total_indices-1).each do |index|
    epsilon, gamma = get_least_most_common_of_index numbers, index
    gamma_rate << gamma
    epsilon_rate << epsilon
  end
  gamma_rate.to_i(2) * epsilon_rate.to_i(2)
end

def get_ratings(numbers, to_check)
    get_ratings_aux(numbers, to_check, 0)
end

def get_ratings_aux(numbers, to_check, index)

  def get_all_of_index_equal_to(numbers, index, common)
    if index > numbers[0].length-1
      raise "WTF r u doin?"
    end
    numbers.select do |num|
      num[index] == common
    end
  end

  def get_common(numbers, index, to_check)
    if numbers.length == 2
      return to_check
    end
    num_0 = 0
    num_1 = 0
    all_of_index = get_all_of_index(numbers, index)
    all_of_index.each do |number|
      if number == "1"
        num_1 += 1
      else
        num_0 += 1
      end
    end
    if to_check == "0"
      num_0 <= num_1 ? "0" : "1"
    else
      num_1 >= num_0 ? "1" : "0"
    end
  end

  if numbers.length == 1
    return numbers[0]
  else
    common = get_common(numbers, index, to_check)
    new_numbers = get_all_of_index_equal_to(numbers, index, common)
    index += 1
    get_ratings_aux(new_numbers, to_check, index)
  end
end

def sol_2(numbers)
  co2_scrub = get_ratings(numbers, "0") 
  oxy_gen = get_ratings(numbers, "1")
  oxy_gen.to_i(2) * co2_scrub.to_i(2)
end

def main
  numbers = take_input
  puts sol_1(numbers)
  puts sol_2(numbers)
end

main