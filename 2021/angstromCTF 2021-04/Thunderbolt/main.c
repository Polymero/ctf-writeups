
undefined8 main(void)

{
  byte bVar1;
  size_t sVar2;
  FILE *pFVar3;
  size_t sVar4;
  void *__ptr;
  void *__ptr_00;
  byte *__ptr_01;
  undefined8 uVar5;
  byte *pbVar6;
  int iVar7;
  char *local_158;
  size_t local_150;
  undefined local_148 [16];
  char local_138 [264];
  
  setvbuf(stdout,(char *)0x0,2,0);
  local_158 = (char *)0x0;
  printf("Enter a string to encrypt: ");
  local_150 = 0;
  getline(&local_158,&local_150,stdin);
  sVar2 = strcspn(local_158,"\n");
  pFVar3 = fopen("flag","rb");
  if (pFVar3 == (FILE *)0x0) {
    puts("Could not open flag file.");
    uVar5 = 1;
  }
  else {
    fgets(local_138,0x100,pFVar3);
    sVar4 = strcspn(local_138,"\n");
    iVar7 = (int)sVar4 + (int)sVar2;
    local_138[(int)sVar4] = '\0';
    __ptr = realloc(local_158,(long)(iVar7 + 1));
    sVar4 = SEXT48(iVar7);
    strcpy((char *)((long)(int)sVar2 + (long)__ptr),local_138);
    pFVar3 = fopen("/dev/urandom","rb");
    fread(local_148,0x10,1,pFVar3);
    __ptr_00 = malloc(sVar4);
    fread(__ptr_00,sVar4,1,pFVar3);
    fgen(__ptr_00,local_148,sVar4,0x10);
    __ptr_01 = (byte *)malloc(sVar4);
    enc(__ptr,__ptr_01,sVar4);
    if (0 < iVar7) {
      pbVar6 = __ptr_01;
      do {
        bVar1 = *pbVar6;
        pbVar6 = pbVar6 + 1;
        printf("%02x",(ulong)bVar1);
      } while (pbVar6 != __ptr_01 + (ulong)(iVar7 - 1) + 1);
    }
    putchar(10);
    free(__ptr_00);
    free(__ptr);
    free(__ptr_01);
    uVar5 = 0;
  }
  return uVar5;
}

