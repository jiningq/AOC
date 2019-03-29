# Random guessing solution for the gold links puzzle on CSE blog posted June 30, 2016
# written in Julia back then, might need some adjustment to run in today's Julia
# should be easily translatable into Python

Pkg.add("Combinatorics")
using Combinatorics

n = 23
x = [2; round(Int, ones(21))];
comb = vcat([collect(combinations(1:n,i)) for i=1:n]...);

function test_eligible(y, target = 23)
	# test whether a combination of lengths can get to all values
	# between 1 and 23. 
	if sum(y) > target
		throw(ArgumentError("Sum of vector greater than the target!"))
	end
	outcome = []
	n = length(y)
	for j in 1:n
		for i in collect(combinations(1:n,j))
			res = sum(y[i])
			if !(res in outcome)
				outcome = [outcome; res]
				if length(outcome) == target
					return true
				end
			end
		end
	end
	return false
end

function merg(y:: Array{Int})
	# randomly merge two links (i.e. summing two items in a list)
	z = copy(y)
	n = length(y)
	picktwo = rand(collect(combinations(1:n, 2)))
	z[n - 1], z[picktwo[1]] = z[picktwo[1]], z[n - 1]
	z[n], z[picktwo[2]] = z[picktwo[2]], z[n]
	z[n - 1] = z[n] + z[n - 1]
	pop!(z)
	return z
end

function evolve(y, target = 23)
	# given a list of lengths, randomly propose merges and
	# return the next 'generation' if it turns out eligible
	if !test_eligible(y, target)
		println(y)
		throw(ArgumentError("Input array isn't eligible!"))
	end
	i = 0
	while i < 600
		i += 1
		cand = merg(y)
		if test_eligible(cand, target)
			#println(i)
			return cand
		end
	end
	return(0)
end

function main(n)
	x = [2; round(Int, ones(21))];
	res = Dict()
	for i in 1:n
		k = 0
		#println(i)
		y = copy(x)
		best = []
		j = 0
		while j < 23
			j = j + 1
			if y != 0
				best = copy(y)
				y = evolve(y)
			end
		end
		if !haskey(res, sort(best))
			println(sort(best))
			k = k + 1
			res[sort(best)] = k
		end
	end
	return res
end

@time main(150)
