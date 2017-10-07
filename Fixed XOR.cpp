
#include "stdafx.h"
#include "hex.h"
#include <string>
#include <iostream>
using namespace std;

int main()

{
	//str1 va etre XOR'ed avec str2
	char str1[] = "1c0111001f010100061a024b53535009181c";
	char temp1[40] = {"0" };
	char str2[] = "686974207468652062756c6c277320657965";
	char temp2[40] = { "0" };
	char finalbin[40] = { "0" };
	char finalhex[40] = { "0" };
	uint32_t l = sizeof(str1) - 1;
	uint32_t l2 = l / 2;
	
	//first on les met en binaire
	Hex::decodeHex((unsigned char *)str1, (unsigned char *)temp1, l);
	Hex::decodeHex((unsigned char *)str2, (unsigned char *)temp2, l);
	


	Hex:: xor ((unsigned char *)temp1, (unsigned char *)temp2, (unsigned char *)finalbin, l2);

	Hex::encodeHex((unsigned char *)finalbin, (unsigned char *)finalhex, l2);
	printf("%s\n", finalhex);

	
	return 0;
	
}


