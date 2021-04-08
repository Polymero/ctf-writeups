
void enc(long param_1,long param_2,long param_3)

{
  uint uVar1;
  int iVar2;
  long lVar3;
  ulong uVar4;
  uint uVar5;
  long lVar6;
  uint uVar7;
  
  if (param_3 != 0) {
    uVar4 = (ulong)s;
    lVar6 = 0;
    uVar5 = 0;
    do {
      lVar3 = (long)(int)uVar5;
      iVar2 = (int)uVar4 + *(int *)(f + lVar3 * 4);
      uVar5 = uVar5 + 1 & 0xff;
      uVar7 = (uint)(iVar2 >> 0x1f) >> 0x18;
      s = *(uint *)(f + (long)(int)((iVar2 + uVar7 & 0xff) - uVar7) * 4);
      uVar7 = (uint)(*(int *)(f + (long)*(int *)(f + (long)(int)s * 4) * 4) + 1 >> 0x1f) >> 0x18;
      *(byte *)(param_2 + lVar6) =
           (byte)*(undefined4 *)
                  (f + (long)(int)((*(int *)(f + (long)*(int *)(f + (long)(int)s * 4) * 4) + 1 +
                                    uVar7 & 0xff) - uVar7) * 4) ^ *(byte *)(param_1 + lVar6);
      uVar4 = SEXT48((int)s);
      lVar6 = lVar6 + 1;
      uVar7 = *(uint *)(f + lVar3 * 4);
      uVar1 = *(uint *)(f + uVar4 * 4);
      *(uint *)(f + lVar3 * 4) = uVar7 ^ uVar1;
      uVar7 = uVar7 ^ uVar1 ^ *(uint *)(f + uVar4 * 4);
      *(uint *)(f + uVar4 * 4) = uVar7;
      *(uint *)(f + lVar3 * 4) = *(uint *)(f + lVar3 * 4) ^ uVar7;
    } while (param_3 != lVar6);
    return;
  }
  return;
}

