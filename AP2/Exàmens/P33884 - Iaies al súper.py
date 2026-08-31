from yogi import tokens, read
from typing import Optional
from collections import deque

class CuaSupermercat:

    def __init__(self) -> None:
        self.cua: deque[str] = deque()
        self.atesos: dict[str, int] = {}

    def arribar(self, client: str) -> None:
        if client[:4] == "Iaia":
            if self.cua:
                ultim = self.cua.pop()
                self.cua.append(client)
                self.cua.append(ultim)
            else:
                self.cua.append(client)
        else:
            self.cua.append(client)


    def atendre(self) -> Optional[str]:
        if self.cua:
            client = self.cua.popleft()
            if client not in self.atesos:
                self.atesos[client] = 0
            self.atesos[client] += 1
            return client
        return None
    
    def escriure_cua(self) -> None:
        print("cua:", end="")
        for client in self.cua:
            print(f' {client}', end="")
        print()
    
    def escriure_clients(self) -> None:
        for client, atesos in sorted(self.atesos.items()):
            print(f'{client} {atesos}')

def main() -> None:
    q = CuaSupermercat()
    for ordre in tokens(str):
        if ordre == "arribar":
            client = read(str)
            q.arribar(client)
            print("arribar", client)
        elif ordre == "atendre":
            temp = q.atendre()
            if temp is None:
                print("cua buida")
            else:
                client = temp
                print("atendre", client)
        elif ordre == "escriure_cua":
            q.escriure_cua()
        elif ordre == "escriure_clients":
            q.escriure_clients()
        else:
            print("Ordre no reconeguda")


if __name__ == "__main__":
    main()