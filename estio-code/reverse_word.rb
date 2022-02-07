puts "Please enter a word to reverse:"
user_word = gets.chomp

word_array = user_word.split("")

if word_array.count >= 5
  puts "Reversing #{user_word}..."
  puts user_word.reverse
else
  puts "Sorry, #{user_word} is too short to reverse."
end
