using Nettle

function md5(msg)
	return hexdigest("md5", msg)
end

salt = "cuanljph"
test = "abc"

function hash2(input)
	for i = 1:2017
		input = hexdigest("md5", input)
	end
	return input
end

function findLetter(hashtext)
	for i = 1:30
		if hashtext[i] == hashtext[i + 1] && hashtext[i + 1] == hashtext[i + 2]
			return hashtext[i]
		end
	end
end

function findLetter1(hashtext)
	return match(r"(.)\1\1", hashtext)
end

function evaluate(i, salt, hashfn = md5)
	hashtext = hashfn(salt * string(i))
	letter = findLetter1(hashtext)
	if letter == nothing
		return false
	else
		for j = i + 1: i + 1000
			hashtext = hashfn(salt * string(j))
			if contains(hashtext, repeat(string(letter), 5))
				return true
			end
		end
		return false
	end
end

function nthkey(salt, hashfn = md5, n = 64)
	seen = 0
	guess = 0
	while seen < n
		guess += 1
		if evaluate(guess, salt, hashfn)
			seen += 1
		end
	end
	return guess
end

@time println(nthkey("abc"))
@time println(nthkey("cuanljph"))


