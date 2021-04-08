
void fgen(long param_1,long param_2,ulong param_3,ulong param_4)

{
  int iVar1;
  long lVar2;
  ulong uVar3;
  uint uVar4;
  ulong uVar5;
  ulong uVar6;
  ulong uVar7;
  
  lVar2 = 0;
  do {
    *(int *)(f + lVar2 * 4) = (int)lVar2;
    lVar2 = lVar2 + 1;
  } while (lVar2 != 0x100);
  uVar3 = (ulong)s;
  uVar6 = 0;
  do {
    uVar7 = uVar6 & 0xff;
    uVar5 = uVar6 + 1;
    iVar1 = (uint)*(byte *)(param_1 + uVar6 % param_3) + (int)uVar3 + *(uint *)(f + uVar7 * 4);
    uVar4 = (uint)(iVar1 >> 0x1f) >> 0x18;
    uVar3 = SEXT48(*(int *)(f + (long)(int)((iVar1 + uVar4 & 0xff) - uVar4) * 4));
    uVar4 = *(uint *)(f + uVar7 * 4) ^ *(uint *)(f + uVar3 * 4);
    *(uint *)(f + uVar7 * 4) = uVar4;
    uVar4 = uVar4 ^ *(uint *)(f + uVar3 * 4);
    *(uint *)(f + uVar3 * 4) = uVar4;
    *(uint *)(f + uVar7 * 4) = *(uint *)(f + uVar7 * 4) ^ uVar4;
    uVar6 = uVar5;
  } while (uVar5 != 0x300);
  uVar6 = 0;
  do {
    uVar5 = uVar6 & 0xff;
    uVar7 = uVar6 + 1;
    iVar1 = (uint)*(byte *)(param_2 + uVar6 % param_4) + (int)uVar3 + *(uint *)(f + uVar5 * 4);
    uVar4 = (uint)(iVar1 >> 0x1f) >> 0x18;
    s = *(uint *)(f + (long)(int)((iVar1 + uVar4 & 0xff) - uVar4) * 4);
    uVar3 = SEXT48((int)s);
    uVar4 = *(uint *)(f + uVar5 * 4) ^ *(uint *)(f + uVar3 * 4);
    *(uint *)(f + uVar5 * 4) = uVar4;
    uVar4 = uVar4 ^ *(uint *)(f + uVar3 * 4);
    *(uint *)(f + uVar3 * 4) = uVar4;
    *(uint *)(f + uVar5 * 4) = *(uint *)(f + uVar5 * 4) ^ uVar4;
    uVar6 = uVar7;
  } while (uVar7 != 0x300);
  return;
}

