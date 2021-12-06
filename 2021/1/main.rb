def take_input
  File.read("input.txt").split.map!(&:to_i)
end

def sol_1(depths)
  incr_count = 0
  (0..depths.length-2).each do |index|
    if depths[index] < depths[index+1]
      # puts "#{depths[index]} < #{depths[index+1]}"
      incr_count += 1
    end
  end
  incr_count
end

def sol_2(depths)
 transformed_depths = depths.map.with_index do |element, index|
  if index >= 2
    element + depths[index - 1] + depths[index - 2]
  end
 end
 sol_1(transformed_depths.compact)
end

def main
  depths = take_input
  puts sol_1(depths)
  puts sol_2(depths)
end

main