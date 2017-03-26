module MaximizeStockProfit

open System
open NUnit.Framework
open FsUnit
open Fuchu

let maxProfit1 p =
    
    let rec loop minSoFar maxProfitSoFar rest =
        match rest with
        | [] -> maxProfitSoFar
        | h :: t ->
            let newMin =
                if (h < minSoFar) then h else minSoFar
            let newMaxProfit =
                let profit = h - minSoFar
                if (profit > maxProfitSoFar) then profit else maxProfitSoFar
            loop newMin newMaxProfit t

    match p with
    | [] | [_] -> failwith "Not enough datapoints"
    | h :: t -> loop h Int32.MinValue t

[<TestFixture>]
type Tests () =

    [<Test>]
    member x.``Basic Tests`` () =
        [ ([2;3], 1); ([3;2], -1); ([5;3;8;0], 5); ([5;4;3;2;1], -1); ([1;2;3;4;3;2;1], 3) ]
        |> List.iter (fun (i, o) -> maxProfit1 i |> should equal o)

    [<Test>]
    member x.``Negative Tests`` () =
        [ []; [2] ]
        |> List.iter
            (fun (i) ->
                (fun () -> maxProfit1 i |> ignore)
                |> should (throwWithMessage "Not enough datapoints") typeof<Exception>)

[<Tests>]
let tests =

    let expect input output _ =
        maxProfit1 input |> should equal output

    let basicTest i (input, output) =
        testCase (sprintf "%i" i) <| expect input output

    let shouldFail input _ =
        maxProfit1 input |> should (throwWithMessage "Not enough datapoints") typeof<Exception>

    let negativeTest i input =
        testCase (sprintf "%i" i) <| shouldFail input

    testList "MaximizeStockProfit" [
        testList "Basic" (
            [ ([2;3], 1); ([3;2], -1); ([5;3;8;0], 5); ([5;4;3;2;1], -1); ([1;2;3;4;3;2;1], 3) ]
            |> List.mapi basicTest
        )
        testList "Negative" (
            [ []; [2] ]
            |> List.mapi negativeTest
        )
    ]