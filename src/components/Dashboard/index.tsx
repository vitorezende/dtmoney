import { Summary } from "../Summary";
import { TransctionTable } from "../TransactionTable";
import { Container } from "./styles";

export function Dashboard () {
  return (
    <Container>
      <Summary />
      <TransctionTable />

    </Container>

  );
}