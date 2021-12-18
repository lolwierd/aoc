=begin
  Create a  class to represent line segments which has an instance method which returns the points which that
  segment passes through.
  Create a 2D array which denotes a grid of points top left being 0,0. 
  Loop through the points of each line segment and increment the grid if the line segement passes through the point.
  So if segment passes through 2,3 increment that position in the array.
=end

class Point
  attr_reader :x, :y

  def initialize(point)
    @x, @y = point.split(',').map(&:to_i)
  end

  def is_further_than(point)
    @x > point.x
  end

end

class Segment 
  attr_reader :start_point, :end_point

  def initialize(points)
    @start_point, @end_point = points.split(" -> ").map {|point| Point.new(point)}
  end

  def is_straight
    if @start_point.x == @end_point.x
      # Vertical line
      1
    elsif @start_point.y == @end_point.y
      # Horizontal line
      0
    else
      nil
    end
  end

  def get_passing_points
    passing_points = []
    line_orientation = is_straight
    if  line_orientation == 1
      start_range, end_range = [@start_point.y, @end_point.y].minmax
      passing_points += (start_range..end_range).map {|y| [@start_point.x, y]}
    elsif line_orientation == 0
      start_range, end_range = [@start_point.x, @end_point.x].minmax
      passing_points += (start_range..end_range).map {|x| [x, @start_point.y]}
    else
      # y = mx + c
      rise = (@end_point.y - @start_point.y)
      run = (@end_point.x - @start_point.x)
      slope = (rise/run)
      intercept = @end_point.y - (slope * @end_point.x)
      start_range, end_range = [@start_point.x, @end_point.x].minmax
      passing_points += (start_range..end_range).map {|x| [x, (slope * x) + intercept]}
    end
    passing_points
  end
end

def take_input(is_trial = false)
  File.read(is_trial ? "trial.txt" : "input.txt").split("\n")
end

def sol_1(segments)
  straight = segments.select do |segment|
    segment.is_straight 
  end
  grid = Hash.new {|hash, key| hash[key] = 0}

  straight.each do |segment|
    segment.get_passing_points.each do |point|
      x, y = point
      grid["#{x}, #{y}"] += 1
    end
  end
  count = 0
  grid.each_value do |value|
    count += 1 if value > 1
  end
  count
end

def sol_2(segments)
  grid = Hash.new {|hash, key| hash[key] = 0}
  segments.each do |segment|
    segment.get_passing_points.each do |point|
      x, y = point
      grid["#{x}, #{y}"] += 1
    end
  end
  count = 0
  grid.each_value do |value|
    count += 1 if value > 1
  end
  count
end

def main
  segments = take_input.map {|segment| Segment.new(segment)}
  puts sol_1(segments)
  puts sol_2(segments)
end

main
