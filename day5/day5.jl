function md5(msg)
	return hexdigest("md5", msg)
end

input = "ffykfhsq"

function getPassword1(input)
	password = ""
	i = 0
	while length(password) < 8
		hashtext = md5(input * string(i))
		if hashtext[1:5] == "00000"
			password *= string(hashtext[6])
			println(i," , ", password)
		end
		i += 1
	end
	return password
end

function getPassword2(input)
	password = ["_" for i in 1:8]
	i = 0
	while "_" in password
		hashtext = md5(input * string(i))
		if hashtext[1:5] == "00000" && isdigit(hashtext[6])
			pos = parse(Int32, hashtext[6])
			if pos < 8 && pos >= 0 && password[pos + 1] == "_"
				password[pos + 1] = string(hashtext[7])
				println(i," , ", join(password))
			end
		end
		i += 1
	end
	return join(password)
end

@time getPassword1("abc")
@time getPassword2("abc")
getPassword1(input)
getPassword2(input)
